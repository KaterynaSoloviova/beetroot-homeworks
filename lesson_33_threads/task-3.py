# Task 3
# Requests using multiprocessing
# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file. For this task use Threads for
# making requests to reddit API.

# Since there is some problem with reddit site, I have used the second task to show how it works using multithreading
# in client

import socket
import threading

SERVER_ADDRESS = "localhost"
SERVER_PORT = 65432
BUFFER_SIZE = 1024


def send_message(message: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_ADDRESS, SERVER_PORT))

        s.sendall(message.encode())

        response = s.recv(BUFFER_SIZE)
        response_message = response.decode()
        print(f"Received from server: {response_message}")


def send_multiple_messages(num_requests: int) -> None:
    threads = []

    for i in range(num_requests):
        thread = threading.Thread(target=send_message, args=(f"Message {i + 1} from client!",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    send_multiple_messages(5)
