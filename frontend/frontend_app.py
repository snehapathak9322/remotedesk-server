import tkinter as tk
import socket
import subprocess
import threading
import time

SERVER_IP = "127.0.0.1"
PORT = 8888

client_socket = None


def connect_to_partner():
    # run connection in background thread
    threading.Thread(target=connect_process).start()


def connect_process():
    global client_socket

    session_id = partner_entry.get()
    status_label.config(text="Status: Connecting...")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, PORT))

        client_socket.sendall(b"CLIENT")
        time.sleep(0.5)
        client_socket.sendall(session_id.encode())

        response = client_socket.recv(1024)

        if response == b"CONNECTED":
            status_label.config(text="Status: Connected!")

            # start viewer automatically
            subprocess.Popen(["python", "controller/screen_viewer.py"])
            subprocess.Popen(["python", "controller/mouse_sender.py"])

        else:
            status_label.config(text="Status: Invalid ID")

    except Exception as e:
        status_label.config(text=f"Error: {e}")


def disconnect():
    global client_socket

    if client_socket:
        client_socket.close()
        status_label.config(text="Status: Disconnected")


# GUI
root = tk.Tk()
root.title("RemoteDesk")
root.geometry("320x220")

title = tk.Label(root, text="RemoteDesk", font=("Arial", 16))
title.pack(pady=10)

my_id = tk.Label(root, text="Your ID: (Run host)")
my_id.pack()

tk.Label(root, text="Enter Partner ID").pack()

partner_entry = tk.Entry(root)
partner_entry.pack()

connect_btn = tk.Button(root, text="Connect", command=connect_to_partner)
connect_btn.pack(pady=5)

disconnect_btn = tk.Button(root, text="Disconnect", command=disconnect)
disconnect_btn.pack()

status_label = tk.Label(root, text="Status: Waiting")
status_label.pack(pady=10)

root.mainloop()