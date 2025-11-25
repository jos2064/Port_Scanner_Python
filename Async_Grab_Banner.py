import asyncio

results = []

async def grab_banner(ip,port,reader,writer):
    try:
        data = await asyncio.wait_for(reader.read(1024), timeout=0.5)
        banner = data.decode(errors="ignore").strip()
        if banner:
            return banner
    
        http_request = (
          "GET / HTTP/1.1\r\n"
          f"Host: {ip}\r\n"
          "User-Agent: AsyncScanner\r\n"
          "Connection: close\r\n\r\n"
        )

        writer.write(http_request.encode())
        await writer.drain()

        data = await asyncio.wait_for(reader.read(1024), timeout=0.5)
        banner = data.decode(errors="ignore").strip()
    
        if banner:
            for line in banner.split("\n"):
                 if "Server:" in line:
                    return line.strip()
            
            return banner
        return None
    
    except:
        return None

async def scan_port(ip,port):
    try:
        reader,writer = await asyncio.wait_for(asyncio.open_connection(ip,port), timeout=0.5)

        print(f"Port {port} is OPEN.")
        banner = await grab_banner(ip,port,reader,writer)

        if banner:
            print(f"---> {banner}")
            results.append((port,banner))
        
        else:
            print("")
            results.append((port,"No banner"))
        
        writer.close()
        await writer.wait_closed()
    except:
        pass

async def scan (ip,start_port,end_port):
    tasks = []
    for port in range(start_port,end_port+1):
        tasks.append(scan_port(ip,port))
    
    await asyncio.gather(*tasks)
    save_results(ip)

def save_results(ip):
    filename= f"{ip}_async_scan_results.txt"
    with open(filename,"w",encoding = "utf-8") as f:
        f.write(f"Scan results for {ip} \n")
        f.write("Ports | Banner \n")
        f.write("-" * 60 +"\n")

        for port,banner in sorted(results):
            f.write(f"{port} : {banner}\n")
    
    print(f"\nResult saved to {filename}")

ip = input("Enter target IP addr:")
start = int(input("Enter start port:"))
end = int(input("Enter end port:"))

asyncio.run(scan(ip,start,end))


    
