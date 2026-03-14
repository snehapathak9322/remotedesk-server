import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = client.recv(1024).decode()
print(msg)

target_id = input("Enter Device ID to connect: ")

client.send(target_id.encode())