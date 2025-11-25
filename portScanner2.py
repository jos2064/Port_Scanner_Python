import socket
import threading
def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip,port))
        print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

def scan(ip):
    for port in range(1,1025):
        t = threading.Thread(target=scan_port, args=(ip, port))
        t.start()

scan("127.0.0.1")