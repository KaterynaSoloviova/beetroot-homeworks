# Task 2
# Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm by a
# specific key obtained from the client.
import socket
from caesar_cipher import caesar_decrypt, caesar_encrypt

SERVER_ADDRESS = "localhost"
SERVER_PORT = 65432
BUFFER_SIZE = 1024
SERVER_SECRET_KEY = 2
CLIENT_SECRET_KEY = 3

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((SERVER_ADDRESS, SERVER_PORT))

    socket.listen()
    print(f"Echo Server listening on {SERVER_ADDRESS}:{SERVER_PORT}...")

    while True:
        client_socket, client_address = socket.accept()
        print(f"Connection established with {client_address}")

        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                print(f"Connection closed by {client_address}")
                break
            encrypted_message = data.decode()
            message = caesar_decrypt(encrypted_message, CLIENT_SECRET_KEY)

            print(f"Received message: {message}")

            decrypted_message = caesar_encrypt(message, SERVER_SECRET_KEY)
            client_socket.sendall(decrypted_message.encode())
