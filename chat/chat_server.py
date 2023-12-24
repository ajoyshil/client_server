import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)

        if not data:
            break
        print("message from client: ", data)
        reply = process_data(data)  # Replace with your server's logic
        conn.sendall(reply)
    conn.close()

def process_data(data):
    # Implement your server's logic to process incoming data and generate a reply
    return data.upper()  # Example: Return the received data in uppercase

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening...")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
