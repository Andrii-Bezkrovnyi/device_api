import requests
import json

url = "http://localhost:8000/devices/1/"
data = {
    "name": "Updated Device Name",
    "type": "Updated Device Type",
    "login": "updated_login",
    "password": "updated_password",
    "location_id": 1,
    "api_user_id": 1
}

response = requests.put(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

if response.status_code == 200:
    print("Device updated successfully:", response.json())
elif response.status_code == 404:
    print("Error: Device not found")
elif response.status_code == 400:
    print("Error: Bad request", response.json())
else:
    print("Error:", response.json())
