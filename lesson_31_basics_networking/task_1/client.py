import socket

SERVER_ADDRESS = "localhost"
SERVER_PORT = 65432
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket:
    message = "Hello, UDP Server!"
    socket.sendto(message.encode(), (SERVER_ADDRESS, SERVER_PORT))
    print(f"Message sent to {SERVER_ADDRESS}:{SERVER_PORT}")

    data, server_address = socket.recvfrom(BUFFER_SIZE)
    response = data.decode()
    print(f"Received response from server: {response}")
