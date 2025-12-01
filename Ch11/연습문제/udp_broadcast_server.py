from socket import *

PORT = 10000

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 172.25.232.96 포함, 이 PC의 모든 NIC에서 10000번 포트로 수신
sock.bind(('', PORT))

print("=== Broadcast Server Listening on UDP port", PORT, "===")

while True:
    msg, addr = sock.recvfrom(1024)
    print("from", addr, ":", msg.decode())
