import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "car_model": "Toyota Innova Hycross",
    "year": 2024,
    "insurance_type": "own_damage"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
