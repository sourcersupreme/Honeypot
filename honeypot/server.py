import socket
from honeypot.logger import log_attack

HOST = "0.0.0.0"
PORT = 9999

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[+] Honeypot running on port {PORT}")

    while True:
        client, addr = server.accept()
        print(f"[!] Connection from {addr}")

        client.send(b"Username: ")
        username = client.recv(1024).strip().decode()

        client.send(b"Password: ")
        password = client.recv(1024).strip().decode()

        log_attack(addr[0], username, password)

        client.send(b"Access Denied!\n")
        client.close()

if __name__ == "__main__":
    start_server()
