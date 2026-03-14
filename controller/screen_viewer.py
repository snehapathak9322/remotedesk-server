import socket
import cv2
import numpy as np
import struct

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for screen stream...")

conn, addr = server.accept()
print("Connected from:", addr)

data = b""
payload_size = struct.calcsize(">L")

cv2.namedWindow("Remote Screen", cv2.WINDOW_NORMAL)

while True:

    # receive message size
    while len(data) < payload_size:
        packet = conn.recv(4096)
        if not packet:
            print("Connection closed")
            conn.close()
            cv2.destroyAllWindows()
            exit()
        data += packet

    packed_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_size)[0]

    # receive frame data
    while len(data) < msg_size:
        packet = conn.recv(4096)
        if not packet:
            print("Connection closed")
            conn.close()
            cv2.destroyAllWindows()
            exit()
        data += packet

    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), 1)

    if frame is not None:
        cv2.imshow("Remote Screen", frame)

    # ESC key to exit
    if cv2.waitKey(1) == 27:
        break

conn.close()
cv2.destroyAllWindows()