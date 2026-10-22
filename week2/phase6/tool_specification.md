
# Phase 06 — From API Integration to Agent Tools

## Task 24 — Define an API Tool

Tool Name: get_post

Description:
Retrieve a post by its unique ID.

HTTP Method:
GET

Endpoint:
https://jsonplaceholder.typicode.com/posts/{post_id}

Required Inputs:
- post_id: Integer identifying the post.

Optional Inputs:
- timeout: Request timeout in seconds (default: 10).

Expected Output:
- id: Post ID
- title: Post title
- body: Post content
- userId: ID of the user who created the post

Possible Errors:
- 400: Bad Request
- 401: Unauthorized
- 404: Post not found
- 429: Rate limit exceeded
- 500: Internal Server Error
- Timeout: Request took too long
- Network Error: Connection or request failure

Authentication Required:
No. JSONPlaceholder does not require an API key for this endpoint.

---

## Task 25 — Design an Agent Tool Interface

Tool: get_post

Purpose:
Retrieve a post using its ID.

Input:
- post_id (integer, required)

Output:
- id (integer)
- title (string)
- body (string)
- userId (integer)

Possible Errors:
- 400: Invalid request
- 401: Authentication failure (if applicable)
- 404: Post not found
- 429: Too many requests
- 500: Server error
- Timeout: Request timed out
- Network Error: Request failed

Tool Behavior:
1. Accept a post_id as input.
2. Send a GET request to the API endpoint.
3. Return the post data if successful.
4. Return an appropriate error message if the request fails.
