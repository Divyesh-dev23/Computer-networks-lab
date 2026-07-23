import socket

HOST = "127.0.0.1"
PORT = 5059

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter file name: ")

client_socket.sendto(filename.encode(), (HOST, PORT))

data, server = client_socket.recvfrom(4096)

print("\nFile Contents:\n")
print(data.decode())

client_socket.close()