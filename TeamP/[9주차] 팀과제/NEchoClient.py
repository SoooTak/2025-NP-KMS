import socket

class NEchoClient:
    def __init__(self, host, port=5050, timeout=5.0):
        self.host = host
        self.port = port
        self.timeout = timeout

    def send_request(self, n, message):
        with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
            f = sock.makefile('rwb', buffering=0)
            req = f"{n}|{message}\n".encode('utf-8')
            f.write(req)

            lines = []
            for _ in range(n):
                line = f.readline()
                if not line:
                    break
                lines.append(line.decode('utf-8').rstrip('\n'))
            return lines

if __name__ == '__main__':
    client = NEchoClient(host='localhost', port=5050)
    resp = client.send_request(3, "Hello World")
    print("Response:")
    for line in resp:
        print(line)