import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("172.25.232.96", 5000)
sock.connect(address)

data = sock.recv(1024).decode().strip()

print("서버 원본 시각 문자열:", data)

parts = data.split()

formatted_time = data  

if len(parts) >= 5:
    weekday = parts[0]   
    month   = parts[1]   
    day     = parts[2]   
    time_str = parts[3]  
    year    = parts[4]   
    formatted_time = f"{year} {month} {day} ({weekday}) {time_str}"

print("현재 시각:", formatted_time)

sock.close()
