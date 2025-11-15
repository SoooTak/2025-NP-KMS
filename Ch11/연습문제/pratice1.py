import telnetlib

HOST = "172.25.232.96"
PORT = 5000

with telnetlib.Telnet(HOST, PORT, timeout=5) as tn:
    data = tn.read_all()
    print("현재 시각:", data.decode("utf-8", errors="ignore").strip())
