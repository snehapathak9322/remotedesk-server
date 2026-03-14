import socket
from pynput import keyboard

HOST = "10.224.203.137"
PORT = 5002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Keyboard control connected")

def on_press(key):
    try:
        message = f"KEY:{key.char}"
        client.send(message.encode())
    except:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()