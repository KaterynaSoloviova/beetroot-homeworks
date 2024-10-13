# Echo server with threading
# Create a socket echo server which handles each connection in a separate Thread.

# Server
import socket
import threading
from typing import Tuple

SERVER_ADDRESS = "localhost"
SERVER_PORT = 65432
BUFFER_SIZE = 1024


def handle_request(client_socket: socket.socket, client_address: Tuple[str, int]) -> None:
    print(f"Connection established with {client_address}")
    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                print(f"Connection closed by {client_address}")
                break

            message = data.decode()
            print(f"Received message: {message}")
            client_socket.sendall(message.encode())

        except ConnectionResetError:
            print(f"Connection closed by {client_address}")
            break
    client_socket.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((SERVER_ADDRESS, SERVER_PORT))

    socket.listen(5)
    print(f"Echo Server listening on {SERVER_ADDRESS}:{SERVER_PORT}...")

    while True:
        client_socket, client_address = socket.accept()

        client_thread = threading.Thread(target=handle_request, args=(client_socket, client_address))
        client_thread.start()
