import requests
import json

def send_post_request(url, data):
    # Convert the data to a JSON string
    json_data = json.dumps(data)

    # Define the headers for the POST request
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the POST request
    response = requests.post(url, data=json_data, headers=headers)

    return response.json().get("result")
