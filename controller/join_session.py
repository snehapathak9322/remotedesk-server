import socket

SERVER_IP = "127.0.0.1"
PORT = 8888

session_id = input("Enter Connection ID: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

client.send(b"CLIENT")
client.send(session_id.encode())

response = client.recv(1024)

if response == b"CONNECTED":
    print("Connected to host!")
else:
    print("Invalid session ID")