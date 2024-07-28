import requests

device_id = input("Enter device id : ")

url = f"http://localhost:8000/devices/{device_id}/"

response = requests.delete(url)

if response.status_code == 200:
    print("Device deleted successfully:", response.json())
elif response.status_code == 404:
    print("Error: Device not found")
else:
    print("Error:", response.json())
