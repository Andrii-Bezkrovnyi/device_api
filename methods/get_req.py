import requests

url = 'http://localhost:8000/devices/'

response = requests.get(url)
print(response.json())
