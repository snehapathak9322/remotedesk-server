import socket
from device_id import get_device_id

SERVER_IP = "127.0.0.1"
PORT = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

device_id = get_device_id()

message = f"HOST:{device_id}"
client.send(message.encode())

print("Your Device ID:", device_id)
print("Waiting for client...")