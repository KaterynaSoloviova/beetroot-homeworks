# Task 1
# During the lesson, we have created a server and client, which use TCP/IP protocol for communication via sockets.
# In this task, you have to create a server and client, which will use user datagram protocol (UDP) for communication.

import socket

SERVER_ADDRESS = "localhost"
SERVER_PORT = 65432
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket:
    socket.bind((SERVER_ADDRESS, SERVER_PORT))

    print(f"UDP Server listening on {SERVER_ADDRESS}:{SERVER_PORT}...")

    while True:
        data, client_address = socket.recvfrom(BUFFER_SIZE)
        message = data.decode()
        print(f"Received message from {client_address}: {message}")

        response = f"Server received: {message}"
        socket.sendto(response.encode(), client_address)
