import socket
port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
while True:
    msg = input("Message to send: ")
    s.send(msg.encode()) #send a message to server
    data = s.recv(BUFSIZE) #receive message from server
    print("Received message: %s" %data.decode())