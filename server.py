import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received packet from {addr}: {data.decode('utf-8')}")
            # Здесь можно обработать данные и, при необходимости, отправить ответ клиенту.
    except Exception as e:
        print(f"Connection error with {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection closed with {addr}")

def start_server():
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SERVER_IP, SERVER_PORT))
        s.listen()
        print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()