# students = [
#     {
#         "id": 1,
#         "name": "Ali"
#     },
#     {
#         "id": 2,
#         "name": "Sara"
#     },
#     {
#         "id": 3,
#         "name": "jhon"
#     }
# ]

# for student in students:
#     print("ID:", student["id"])
#     print("Name:", student["name"])



# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print("Status:", response.status_code)

# if response.status_code == 200:
#     post = response.json()

#     print("Post ID:", post["id"])
#     print("Title:", post["title"])
#     print("Body:", post["body"])    


# import requests

# for i in range(1, 4):
#     url = f"https://jsonplaceholder.typicode.com/posts/{i}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         post = response.json()
#         print(f"Post {i}: {post['title']}")
#     else:
#         print(f"Failed to retrieve Post {i}")


import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()

    print("Total Posts:", len(posts))

    for post in posts[:5]:
        print(post["title"])
else:
    print("Failed to retrieve posts")