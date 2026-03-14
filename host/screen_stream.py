import socket
import mss
import numpy as np
import cv2
import struct
import time

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wait until viewer starts
while True:
    try:
        client.connect((HOST, PORT))
        print("Connected to viewer")
        break
    except:
        print("Waiting for viewer...")
        time.sleep(2)

sct = mss.mss()
monitor = sct.monitors[1]

while True:
    # capture screen
    screenshot = sct.grab(monitor)

    frame = np.array(screenshot)

    # convert BGRA → BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    # compress frame
    _, buffer = cv2.imencode('.jpg', frame)

    data = buffer.tobytes()

    # send frame size first
    message = struct.pack(">L", len(data)) + data

    try:
        client.sendall(message)
    except:
        print("Connection lost")
        break