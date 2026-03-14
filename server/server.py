import socket
from utils.session_manager import register_device, get_device

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started...")

while True:
    client, address = server.accept()

    print("Device connected:", address)

    device_id = register_device(client)

    client.send(f"DEVICE_ID:{device_id}".encode())