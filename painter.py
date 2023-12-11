import cv2
import numpy as np
import time
import os 
import calcMath as CM
import track_hands as TH
import imageToTextFa as ITF
import requests
import postRequest as PR

brush_thickness = 15
eraser_thickness = 100
image_canvas =np.zeros((720,1280,3), np.uint8)
currentT=0
previousT =0

header_img = "Images"
header_img_list = os.listdir(header_img)
overlay_image =[]


for i in header_img_list:
    image = cv2.imread(f'{header_img}/{i}')
    overlay_image.append(image)

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

cap.set(cv2.CAP_PROP_FPS, 60)

default_overlay = overlay_image[0]
draw_color = (255,105,65)

detector= TH.handDetector(min_detection_confidence=.85)

xp =0
yp=0
# fullAns = ""
counter_confirm = 0
while True:
    # answer = ""
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame[0:125,0:1280] = default_overlay

    frame = detector.findHands(frame, draw=True)
    landmark_list = detector.findPosition(frame, draw =False)

    if(len(landmark_list)!=0):
        x1, y1 =(landmark_list[8][1:]) #index
        x2, y2 = landmark_list[12][1:] #middle    
        # x3, y3 = landmark_list[14][1:] #3    
        # print(x3,'-----',y3)

        my_fingers = detector.fingerStatus()
        # cv2.rectangle(frame, (0, 460), (250, 530), (0,0,0), -1)
        # cv2.putText(frame, str(my_fingers), (0,500), fontFace= cv2.FONT_HERSHEY_COMPLEX, color= (255,255,255), thickness=2, fontScale=1)
        cv2.putText(frame, f"Counter Confirm:{str(counter_confirm)}", (0,150), fontFace= cv2.FONT_HERSHEY_COMPLEX, color= (255,0,0), thickness=2, fontScale=1)
        if (not(my_fingers[1] or my_fingers[2] or my_fingers[3] or my_fingers[4])):
            xp , yp = x1, y1
        if (my_fingers[1] and my_fingers[2] and not my_fingers[3] and not my_fingers[4]):
            xp, yp = 0,0
            if (y1<125):
                if(200<x1<340):
                    default_overlay = overlay_image[0] 
                    draw_color = (255,0,0)
                elif (340<x1<500):
                    default_overlay = overlay_image[1]
                    draw_color = (47,225,245)
                elif (500<x1<640):
                    default_overlay = overlay_image[2]
                    draw_color = (197,47,245)
                elif (640<x1<780):
                    default_overlay = overlay_image[3]
                    draw_color = (53,245,47)
                elif (1100<x1<1280):
                    default_overlay = overlay_image[4]
                    draw_color = (0,0,0)

            cv2.putText(frame, 'Selector Mode', (900,680), fontFace=cv2.FONT_HERSHEY_COMPLEX, color= (0,255,255), thickness=2, fontScale=1)
            cv2.line(frame, (x1,y1), (x2,y2), color=draw_color, thickness=3)

        if (my_fingers[1] and not my_fingers[2] and not my_fingers[3] and not my_fingers[4]):
                    
            cv2.putText(frame, "Writing Mode", (900,680), fontFace= cv2.FONT_HERSHEY_COMPLEX, color= (255,255,0), thickness=2, fontScale=1)
            cv2.circle(frame, (x1,y1),15, draw_color, thickness=-1)
            if xp ==0 and yp ==0:
                xp =x1 
                yp =y1
            
            if draw_color == (0,0,0):
                cv2.line(frame, (xp,yp),(x1,y1),color= draw_color, thickness=eraser_thickness)
                cv2.line(image_canvas, (xp,yp),(x1,y1),color= draw_color, thickness=eraser_thickness)

            else:
                cv2.line(frame, (xp,yp),(x1,y1),color= draw_color, thickness=brush_thickness)
                cv2.line(image_canvas, (xp,yp),(x1,y1),color= draw_color, thickness=brush_thickness)
            
            xp , yp = x1, y1

        if (my_fingers[1] and my_fingers[2] and my_fingers[3] and my_fingers[4]):
            cv2.putText(frame, f"Saving Mode", (900,680), fontFace= cv2.FONT_HERSHEY_COMPLEX, color= (0,255,0), thickness=2, fontScale=1)
            counter_confirm+=1
            if counter_confirm>=100:
                now = time.time()
                imageName = str(now)+'saved_drawing.png'
                cv2.imwrite('savedPaintings/'+imageName,image_canvas)
                cv2.imshow('What you have painted', image_canvas)
                cv2.waitKey(60*1000)
                cv2.destroyAllWindows()
                uploadFile =""
                with open('savedPaintings/'+imageName, "rb") as image_file:
                    file_data = {
        "file": ("image.png", image_file, "image/png")
    }

                    uploadFile = PR.send_request(file_data=file_data)
                print(uploadFile)
                dataFrom1 = ITF.send_post_request("https://www.eboo.ir/api/ocr/getway",{
    "token":"6Ijtw8NJlrra4F93DM0PbJEfii0SzwyH",
    "command":"addfile",
    "filelink":uploadFile.get("files")[0].get("fileUrl")
})
                print(dataFrom1)
                fileToken = dataFrom1.get("FileToken")
                convertMethods = int(dataFrom1.get("ConvertMethods"))
                dataFrom2 = ITF.send_post_request("https://www.eboo.ir/api/ocr/getway",{
    "token":"6Ijtw8NJlrra4F93DM0PbJEfii0SzwyH",
    "command":"convert",
    "filetoken":fileToken,
    "method":convertMethods,
    "output":"txt"
})
                print(dataFrom2)
                receviedTxt = requests.get(dataFrom2.get("FileToDownload"))

                with open(f'convertedToText/{str(now)}.txt', 'wb') as file:
                    file.write(receviedTxt.content)
                    
                    
                image_canvas =np.zeros((720,1280,3), np.uint8)
                counter_confirm=0
                
                


                

    img_gray = cv2.cvtColor(image_canvas, cv2.COLOR_BGR2GRAY)
    _, imginv= cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    imginv = cv2.cvtColor(imginv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, imginv)
    frame =cv2.bitwise_or(frame, image_canvas)
    currentT = time.time()
    fps = 1/(currentT- previousT)
    previousT = currentT

    # cv2.putText(frame, 'Prev Calculation:' + str(fullAns), (10,670), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,0,0), thickness=2)


    cv2.imshow('paint', frame)
    cv2.waitKey(1)

