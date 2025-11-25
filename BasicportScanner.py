import socket

def scan_port(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((ip, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} is closed")
    finally:
        s.close()

scan_port("127.0.0.1", 135)

