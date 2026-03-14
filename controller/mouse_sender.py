import socket
from pynput import mouse

HOST = "10.224.203.137"   # remote PC IP
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to host for mouse control")

def on_move(x, y):
    try:
        message = f"MOVE:{x}:{y}"
        client.send(message.encode())
    except:
        print("Connection lost")
        return False

def on_click(x, y, button, pressed):
    try:
        if pressed:
            message = f"CLICK:{x}:{y}"
            client.send(message.encode())
    except:
        return False

listener = mouse.Listener(on_move=on_move, on_click=on_click)
listener.start()
listener.join()