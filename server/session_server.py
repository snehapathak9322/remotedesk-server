import socket
import threading

HOST = "0.0.0.0"
PORT = 8888

sessions = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Session Server Running...")

def handle_client(conn, addr):
    print("Connected:", addr)

    try:
        data = conn.recv(1024).decode().strip()
        print("Data received:", data)

        # ---------------- HOST REGISTRATION ----------------
        if data.startswith("HOST:"):
            device_id = data.split(":")[1]

            sessions[device_id] = conn

            print("Host registered with ID:", device_id)

            # Keep host waiting for client
            while True:
                pass

        # ---------------- CLIENT CONNECTION ----------------
        elif data == "CLIENT":

            session_id = conn.recv(1024).decode().strip()
            print("Session ID received:", session_id)

            if session_id in sessions:

                host_conn = sessions[session_id]

                host_conn.sendall(b"START_SESSION")
                conn.sendall(b"CONNECTED")

                print("Client joined session:", session_id)

            else:
                conn.sendall(b"INVALID")
                print("Invalid ID attempt:", session_id)

    except Exception as e:
        print("Error:", e)

    finally:
        pass


while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()