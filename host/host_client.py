import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = client.recv(1024).decode()

if msg.startswith("DEVICE_ID"):
    device_id = msg.split(":")[1]
    print("Your Device ID:", device_id)

while True:
    pass