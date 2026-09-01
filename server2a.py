import socket

HOST = "127.0.0.1"
PORT = 5056

server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))

server_socket.listen(5)

print("Server is listening...")

while True:
    client_socket , address = server_socket.accept()
    print("Connected to:", address)
    filename = client_socket.recv(1024).decode()

    try:
        with open(filename , "r") as file:
            data = file.read()

    except FileNotFoundError:
        data = "File not found"
    
    client_socket.send(data.encode())

    client_socket.close()
    print("Connection closed.\n")