import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "message": "Hey, are you coming to college tomorrow?"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())