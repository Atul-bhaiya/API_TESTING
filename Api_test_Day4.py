import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()

post_id = posts[0]["id"]
print("Post ID to delete:", post_id)

delete_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
delete_response = requests.delete(delete_url)

print("Status Code:", delete_response.status_code)
print("Response:", delete_response.json())

assert delete_response.status_code == 200
