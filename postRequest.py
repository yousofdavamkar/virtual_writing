import requests
import secrets
def send_request(file_data):
    url = "https://api.bytescale.com/v2/accounts/W142iNB/uploads/form_data"
    headers = {
        "Authorization": "Bearer public_W142iNB9rSFVtRD8FA4FBCZ9PsFJ",
    }

    files = file_data

    response = requests.post(url, headers=headers, files=files)

    return response.json()
