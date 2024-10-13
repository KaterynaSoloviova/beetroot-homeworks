# Echo server with threading
# Create a socket echo server which handles each connection in a separate Thread.

# Client

import socket

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


send_message("Message from client!")
