import socket

HOST = "127.0.0.1"
PORT = 5056

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

filename = input("Enter file name: ")

client_socket.send(filename.encode())

data = client_socket.recv(4096).decode()

print("\nFile Contents:\n")
print(data)

client_socket.close()