import socket

SERVER_IP = "172.25.232.96"
SERVER_PORT = 5000
ADDR = (SERVER_IP, SERVER_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.sendto(b"TIME", ADDR)

    data, server_addr = sock.recvfrom(1024)
    raw_time = data.decode().strip()

    print("서버 원본 시각 문자열:", raw_time)

    parts = raw_time.split()

    formatted_time = raw_time  

    if len(parts) >= 5:
        weekday = parts[0] 
        month   = parts[1]   
        day     = parts[2]  
        time_str = parts[3]  
        year    = parts[4]   

        formatted_time = f"{year} {month} {day} ({weekday}) {time_str}"

    print("현재 시각:", formatted_time)

finally:
    sock.close()
