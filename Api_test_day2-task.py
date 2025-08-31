import requests

Api = "https://jsonplaceholder.typicode.com/users"
response = requests.get(Api)
user = response.json()
print(user[0]["id"])
print(response.status_code)
assert response.status_code == 200
Data = {
  "title": "API Testing Challenge",
  "body": "Learning GET + POST together",
    "userId": user[0]["id"]
}
post_url = "https://jsonplaceholder.typicode.com/posts"
response2 = requests.post(post_url, json=Data)
print(response2.status_code)
print(response2.json())
assert response2.status_code == 201




