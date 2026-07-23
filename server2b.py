import socket

HOST = "127.0.0.1"
PORT = 5059

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((HOST, PORT))

print("UDP Server is listening...")

while True:
    filename, client_address = server_socket.recvfrom(1024)

    print("\nClient Connected:", client_address)

    filename = filename.decode()
    print("Requested File:", filename)

    try:
        with open(filename, "r") as file:
            data = file.read()
        print("File found. Sending file contents...")
    except FileNotFoundError:
        data = "File not found."
        print("File not found.")

    server_socket.sendto(data.encode(), client_address)

    print("Response sent to client.")
    print("-----------------------------------")