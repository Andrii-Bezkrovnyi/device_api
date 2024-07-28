import requests

url = 'http://localhost:8000/devices/'
headers = {'Content-Type': 'application/json'}
data = {
    "name": "New Device",
    "type": "Sensor",
    "login": "device_login",
    "password": "device_password",
    "location_id": 1,
    "api_user_id": 1
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
