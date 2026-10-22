import requests
import time

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10
MAX_RETRIES = 2


def get_post(post_id):
    if not isinstance(post_id, int) or post_id < 1:
        print("Invalid post ID. Enter a positive integer.")
        return

    url = f"{BASE_URL}/posts/{post_id}"

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.get(url, timeout=TIMEOUT)
            status = response.status_code

            if status == 429:
                if attempt < MAX_RETRIES:
                    delay = int(response.headers.get("Retry-After", 2))
                    delay = min(max(delay, 0), 30)
                    print(f"Rate limit reached. Retrying in {delay} seconds.")
                    time.sleep(delay)
                    continue

                print("Too many requests (429). Try again later.")
                return

            if status == 400:
                print("Bad Request (400).")
                return

            elif status == 401:
                print("Unauthorized (401).")
                return

            elif status == 404:
                print("Resource not found (404).")
                return

            elif status == 500:
                print("Internal Server Error (500).")
                return

            elif response.ok:
                data = response.json()

                print("Request successful!")
                print("ID:", data.get("id"))
                print("User ID:", data.get("userId"))
                print("Title:", data.get("title"))
                print("Body:", data.get("body"))
                return

            else:
                print("API error. Status Code:", status)
                return

        except requests.exceptions.Timeout:
            print("Request timed out.")
            return

        except requests.exceptions.RequestException as error:
            print("Network/request failure:", error)
            return

        except ValueError:
            print("Invalid JSON response.")
            return

if __name__ == "__main__":
    try:
        post_id = int(input("Enter post ID (1 for success, 999999 for 404): "))
        get_post(post_id)
    except ValueError:
        print("Please enter a valid integer.")
