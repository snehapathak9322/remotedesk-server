import socket
import pyautogui

HOST = "0.0.0.0"
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for keyboard connection...")

conn, addr = server.accept()
print("Keyboard connected:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    if data.startswith("KEY:"):
        key = data.split(":")[1]
        pyautogui.press(key)