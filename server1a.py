import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1", 12345))

print("UDP Server is running...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print("Received from Client:", message)

    uppercase_message = message.upper()

    server_socket.sendto(uppercase_message.encode(), client_address)