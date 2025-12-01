#TCP_echoserver.py
from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)
print("클라이언트를 기다리는중..")

c_sock, (r_host, r_port) = sock.accept()
print('connected by', r_host, r_port)
while True:
    try:
        data = c_sock.recv(BUFSIZE)
        if not data:
            c_sock.close()
            print('연결이 종료되었습니다')
            break
    except:
        print("연결이 종료되었습니다")
        c_sock.close()
        break
    else:
        print(data.decode())
    
    try:
        c_sock.send(data)
    except:
        print("연결이 종료되었습니다.")
        c_sock.close()
        break