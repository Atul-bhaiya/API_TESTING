
import requests

Url = "https://jsonplaceholder.typicode.com/posts/2"
response = requests.get(Url)
print(response.status_code)
assert response.status_code == 200
data = response.json()
print(data["title"])
print(data["body"])