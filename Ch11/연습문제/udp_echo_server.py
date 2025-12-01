import socket

SERVER_IP = "172.25.232.96"
PORT = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, PORT))

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print("Received message:", data.decode())
    sock.sendto(data, addr)
