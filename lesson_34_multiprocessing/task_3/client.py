# Task 3
# Echo server with threading
# Create a socket echo server that handles each connection using the multiprocessing library.

import socket
import multiprocessing

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
    processes = []

    for i in range(num_requests):
        process = multiprocessing.Process(target=send_message, args=(f"Message {i + 1} from client!",))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    send_multiple_messages(3)
