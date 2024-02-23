import requests
import time

def check_server_up(url):
    try:
        response = requests.get(url)
        if response.status_code == 500:
            return False
        else:
            return True
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Get the server URL from the user
server_url = input("Enter the URL of the server you want to check: ")

while True:
    if check_server_up(server_url):
        print("Server is up!")
    else:
        print("Server is down or unreachable.")
    time.sleep(5)  # Pause for 5 seconds before the next check
