# Task 2
# Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm by a
# specific key obtained from the client.

import socket
from caesar_cipher import caesar_encrypt, caesar_decrypt

SERVER_ADDRESS = "localhost"
SERVER_PORT = 65432
BUFFER_SIZE = 1024
CLIENT_SECRET_KEY = 3
SERVER_SECRET_KEY = 2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((SERVER_ADDRESS, SERVER_PORT))

    message = input("Please write the massage: ")
    encrypted_message = caesar_encrypt(message, CLIENT_SECRET_KEY)
    socket.sendall(encrypted_message.encode())

    response = socket.recv(BUFFER_SIZE)
    encrypted_message = response.decode()
    message = caesar_decrypt(encrypted_message, SERVER_SECRET_KEY)
    print(f"Received from server: {message}")
