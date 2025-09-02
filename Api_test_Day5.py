import requests

Url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(Url)
users = response.json()
user_id = users[0]["id"]
print(user_id)
print(response.status_code)

user_url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
user_response = requests.get(user_url)
print(user_response.status_code)
assert user_response.status_code in [200,201]
print("Posts of User:", user_response.json()[:2])  