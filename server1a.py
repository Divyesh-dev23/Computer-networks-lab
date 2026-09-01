import socket

server_socket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1" , 12345))

print("UDP is runnning...")

while True:
    data , client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print("Messaged recieved from client:",message)

    upper_message = message.upper()

    server_socket.sendto(upper_message.encode(),client_address)