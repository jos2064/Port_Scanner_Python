import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip,port):
    try:
        s = socket.socket()
        s.settimeout(0.3)
        s.connect((ip,port))
        print(f"Port {port} is OPEN")
    except:
        pass
    finally:
        s.close()

def scan(ip,start_port,end_port):
    THREADS = 100
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for port in range(start_port,end_port + 1):
            executor.submit(scan_port,ip,port)


target = input("Enter IP:")
start  = int(input("Enter starting port:"))
end = int(input("Enter end port:"))

scan(target,start,end)