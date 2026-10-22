
# Final Integration Project — Python API Client

## API Details

- API: JSONPlaceholder
- Endpoint: https://jsonplaceholder.typicode.com/posts/{post_id}
- HTTP Method: GET
- Required Parameter: post_id (positive integer)
- Optional Parameters: None
- Request Body: None
- Authentication: Not required

## Response Structure

The API returns a JSON object containing:

- id: Post ID
- userId: ID of the post author
- title: Post title
- body: Post content

## Error Handling

- 400: Bad Request
- 401: Unauthorized
- 404: Resource Not Found
- 429: Too Many Requests
- 500: Internal Server Error
- Timeout: Request takes too long
- Network Error: Connection or request failure
- Invalid JSON: Response cannot be parsed

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the application:

python src/api_client.py

Enter 1 to retrieve a post or 999999 to test a 404 response.

## Future Agent Tool

Tool Name: get_post

Purpose: Retrieve a post by its ID.

Input:
- post_id (integer)

Output:
- id
- userId
- title
- body

Possible Errors:
- 400, 401, 404, 429, 500
- Timeout
- Network failure
- Invalid JSON

An AI agent could later call this operation as a tool,
provide a post ID, and receive structured post data.
The current project does not implement an AI agent.
