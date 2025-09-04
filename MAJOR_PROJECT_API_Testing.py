import requests



def test_get():
    get_url = "https://jsonplaceholder.typicode.com/users"
    get_response = requests.get(get_url)
    print(get_response.status_code)
    data = get_response.json()
    print("First User:", data[0])
    assert get_response.status_code == 200
    print("Get Method Worked Successfully ")

def test_post():
    post_url ="https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "API Testing Major Project",
        "body": "Testing POST request with pytest",
        "userId": 1
    }
    post_response = requests.post(post_url , json=payload)
    print(post_response.status_code)
    print(post_response.json())

    assert post_response.status_code == 201
    print("Post response worked successfully ")


def test_put():
    post_url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Temp Post for Update",
        "body": "This post will be updated",
        "userId": 1
    }
    post_response = requests.post(post_url, json=payload)
    assert post_response.status_code == 201
    post_id = post_response.json()["id"]
    print("Created Post ID:", post_id)

    put_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    put_payload = {
        "title": "Atul Bhaiya Major Project",
        "body": "Testing PUT request with pytest",
        "userId": 1
    }
    put_response = requests.put(put_url, json=put_payload)

    print(put_response.status_code)
    print(put_response.json())
    assert put_response.status_code == 200
    print("PUT Method Worked Successfully")

def test_delete():
    post_url = "https://jsonplaceholder.typicode.com/posts"
    payload =  {
        "title": "Atul Bhaiya Major Project",
        "body": "Testing PUT request with pytest",
        "userId": 1
    }
    post_response = requests.post(post_url, json=payload)
    assert post_response.status_code == 201
    post_id = post_response.json()["id"]
    print("Post Created for Deletion:", post_id)

    delete_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    delete_response = requests.delete(delete_url)
    print("Delete Status Code:", delete_response.status_code)

    assert delete_response.status_code in [200, 204]
    print("Post Deleted Successfully ")
