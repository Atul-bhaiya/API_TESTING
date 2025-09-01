import requests

Url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(Url)
posts = response.json()

post_id = posts[0]["id"]
print("Post ID:", post_id)

update_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

data = {
    "title": "Updated Title by Atul",
    "body": "This post has been updated successfully!"
}

put_response = requests.put(update_url, json=data)
print("Status Code:", put_response.status_code)
print("Response JSON:", put_response.json())

assert put_response.status_code == 200
