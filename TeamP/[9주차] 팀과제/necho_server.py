#necho_server.py
import socket
import threading

class ClientHandler(threading.Thread):
    def __init__(self, conn, addr, max_n=1000):
        super().__init__(daemon=True)
        self.conn = conn
        self.addr = addr
        self.max_n = max_n

    def run(self):
        try:
            f = self.conn.makefile('rwb', buffering=0)
            line = f.readline()
            if not line:
                return
            try:
                text = line.decode('utf-8').rstrip('\n')
                if '|' not in text:
                    self._write_line(f, "ERR|BAD_REQUEST")
                    return
                n_str, msg = text.split('|', 1)
                n = int(n_str)
                if not (1 <= n <= self.max_n):
                    self._write_line(f, "ERR|N_OUT_OF_RANGE")
                    return
            except Exception:
                self._write_line(f, "ERR|BAD_REQUEST")
                return

            for _ in range(n):
                self._write_line(f, msg)
        finally:
            self.conn.close()

    def _write_line(self, f, s):
        f.write((s + '\n').encode('utf-8'))

class NEchoServer:
    def __init__(self, host='0.0.0.0', port=5050, backlog=128):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.sock = None

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 재시작 편의
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.backlog)
        print(f"[SERVER] Listening on {self.host}:{self.port}")

        try:
            while True:
                conn, addr = self.sock.accept()
                print(f"[SERVER] Connected: {addr}")
                ClientHandler(conn, addr).start()
        except KeyboardInterrupt:
            print("\n[SERVER] Shutting down...")
        finally:
            self.sock.close()

if __name__ == '__main__':
    NEchoServer().start()
