# Quick script to POST to http://localhost:8000/predict

import requests

url = "http://localhost:8000/predict"
data = {"input":"Hello world!"}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())