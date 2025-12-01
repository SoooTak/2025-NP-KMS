#frame_parsing.py
import socket
import capsule

SIZE = 5
sock = socket.socket()
sock.setblocking(True)
sock.settimeout(0, 1)
sock.connect(('127.0.0.1', 2500))

header = {"START": 0x05, "ADDR": 1, "NO": 1, "LENGTH": SIZE}
header_size = 11

frame_seq = ""
msg = "hello world"
print("전송 메시지: ", msg)

for i in range(0, len(msg), SIZE) :
    start = i
    frame_seq += capsule.frame(header["START"], header["ADDR"], header["NO"], msg[start:start+SIZE])
    start += SIZE
    header["NO"] += 1
    
sock.send(frame_seq.encode())

r_msg = ''
seq_num = 1
while True:
    try:
        if sock.recv(1).decode() == chr(0x05):
            p_msg = sock.recv(header_size-1).decode()
            
            if int(p_msg[2:6]) == seq_num:
                payload_len = int(p_msg[-4:])
                r_msg = r_msg + sock.recv(payload_len).decode()
                seq_num += 1
    except:
        break

print("복원 메시지: ", r_msg)
sock.close()
