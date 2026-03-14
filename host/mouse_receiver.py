import socket
import pyautogui

HOST = "0.0.0.0"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for mouse connection...")

conn, addr = server.accept()
print("Controller connected:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    parts = data.split(":")

    if parts[0] == "MOVE":
        x = int(parts[1])
        y = int(parts[2])
        pyautogui.moveTo(x, y)

    elif parts[0] == "CLICK":
        x = int(parts[1])
        y = int(parts[2])
        pyautogui.click(x, y)