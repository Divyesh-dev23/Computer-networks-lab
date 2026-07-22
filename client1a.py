import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 12345)

message = input("Enter a line: ")

client_socket.sendto(message.encode(), server_address)

data, _ = client_socket.recvfrom(1024)

print("Server Response:", data.decode())

client_socket.close()