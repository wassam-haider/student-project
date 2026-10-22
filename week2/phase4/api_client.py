# # ### Public API

# 1. Credentials required: no credentials are required.
# 2. Why authentication is used: Authentication is usually not required because the API allows public access.
# 3. Example authentication mechanism: No authentication required.
# 4. Invalid credentials: Not applicable if authentication is not required.

# ### Protected API

# 1. Credentials required: Credentials are required to access protected resources.
# 2. Why authentication is used: To verify users and prevent unauthorized access.
# 3. Example authentication mechanism: API keys or JWT.
# 4. Invalid credentials: The server rejects the request, usually with a `401 Unauthorized` or `403 Forbidden` status code.


# import requests

# url = "https://api.example.com/students/101"
# token = "YOUR_TOKEN_HERE"

# headers = {
#     "Authorization": f"Bearer {token}"
# }

# request = requests.Request("GET", url, headers=headers)
# prepared_request = request.prepare()

# print("Method:", prepared_request.method)
# print("Endpoint:", prepared_request.url)
# print("Request Headers:", {
#     "Authorization": "Bearer [REDACTED]"
# })



import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if api_key:
    print("API key loaded successfully")
else:
    print("API key not found")
