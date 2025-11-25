import socket 
import threading

def grab_banner(ip,port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip,port)) 

        try:
            banner = s.recv(1024).decode().strip()
            if banner:
                return banner
        except:
            pass

        try:
            http_request = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
            s.send(http_request)
            data = s.recv(1024).decode(errors="ignore").strip()
            if "Server:" in data:
                for line in data.split("\n"):
                    if  "Server:" in line:
                        return line.strip()
            return None
        except:
            return None
    except:
        return None
    finally:
        s.close()

def scan_port(ip,port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip,port))
        print(f"Port {port} is OPEN", end ="")
        banner = grab_banner(ip,port)
        if banner:
            print(f"- {banner}")
        else:
            print("")
    except:
        pass

def scan(ip,start_port,end_port):
    threads = []
    for port in range(start_port,end_port+ 1):
        t = threading.Thread(target=scan_port, args=(ip,port))
        t.daemon = True
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

target = input("Enter target IP:")

start = int(input("Start port:"))
end = int(input("End port:"))

scan(target,start,end)