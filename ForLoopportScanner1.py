import socket

def scan(ip):
    for port in range(1,1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((ip,port))
            print(f"Port {port} is OPEN")
            s.close()
        except:
            pass

scan("127.0.0.1")
