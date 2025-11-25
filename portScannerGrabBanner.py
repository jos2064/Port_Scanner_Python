import socket
def grab_banner(ip,port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip,port))
        try:
            banner = s.recv(1024).decode().strip()
            return banner
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
        print(f"Port {port} is OPEN", end="")

        banner = grab_banner(ip,port)
        if banner:
           print(F"Banner - {banner}")
        else :
           print("")
    except:
      pass
    
def scan(ip):
    for port in range(1,1025):
        scan_port(ip,port)

target = input("Enter Target IP: ")
scan(target)
    
    


