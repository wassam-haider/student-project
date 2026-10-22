# import requests

# url = "https://jsonplaceholder.typicode.com/posts/999999"

# try:
#     response = requests.get(url, timeout=10)

#     if response.status_code == 404:
#         print("Request failed.")
#         print("Status Code:", response.status_code)
#         print("Resource not found.")
#     else:
#         print("Status Code:", response.status_code)

# except requests.exceptions.RequestException:
#     print("Request failed due to a network error.")


# import requests

# url = "https://jsonplaceholder.typicode.com/posts/999999"

# try:
#     response = requests.get(url, timeout=10)
#     status_code = response.status_code

#     if 200 <= status_code < 300:
#         print("Request successful.")
#         print("Status Code:", status_code)

#     elif status_code == 400:
#         print("Bad Request. The request is invalid.")

#     elif status_code == 401:
#         print("Unauthorized. Authentication is required or invalid.")

#     elif status_code == 404:
#         print("Request failed.")
#         print("Status Code:", status_code)
#         print("Resource not found.")

#     elif status_code == 429:
#         print("Too Many Requests. Rate limit exceeded.")

#     elif status_code == 500:
#         print("Internal Server Error. Please try again later.")

#     else:
#         print("Unexpected HTTP response.")
#         print("Status Code:", status_code)

# except requests.exceptions.Timeout:
#     print("Request timed out.")

# except requests.exceptions.RequestException:
#     print("Request failed due to a network error.")


# timeout prevent programs from waiting indefinetly

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)

    if response.ok:
        print("Request successful.")
    else:
        print("API error. Status Code:", response.status_code)

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.RequestException:
    print("Network/request failure.")


# 1\. Rate limit: A restriction on how many API requests a client can make within a specific time period.

# 2\. Why APIs impose rate limits: To prevent abuse, reduce server overload, and ensure fair access for users.

# 3\. HTTP 429: Means “Too Many Requests,” indicating that the client has exceeded the allowed request rate.

# 4\. Why automated programs generate too many requests: Loops, retries, or repeated API calls can send requests rapidly without delays.

# 5\. Importance for agentic systems: AI agents can autonomously execute many tool calls and retries, potentially exhausting API limits and disrupting workflows.