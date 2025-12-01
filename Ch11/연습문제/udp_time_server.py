import socket
import time

HOST = ""
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP Time Server listening on port {PORT}...")

while True:
    data, addr = sock.recvfrom(1024)
    now_str = time.ctime()
    sock.sendto(now_str.encode("utf-8"), addr)
