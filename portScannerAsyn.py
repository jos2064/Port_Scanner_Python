# import asyncio
# async def scan_port(ip,port):
#     try:
#         reader, writer = await asyncio.wait_for(asyncio.open_connection(ip,port),timeout=0.5)
#         print  (f"Port {port} is open")
#         writer.close()
#         await writer.wait_closed()
#     except:
#         pass
    
# async def scan(ip,start_port,end_port):
#     tasks = []
#     for port in range(start_port,end_port + 1):
#         tasks.append(scan_port(ip,port))

#     await asyncio.gather(*tasks)

# ip = input("Enter target IP:")
# start = int(input("Enter start port:"))
# end = int(input("Enter end port:"))

# asyncio.run(scan(ip,start,end))

import asyncio
open_ports = []
async def scan_port(ip,port):
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(ip,port),timeout=0.5)
        print(f"Port {port} is OPEN")
        open_ports.append(port)
        writer.close()
        await writer.wait_closed()
    except:
        pass

async def scan(ip,start_port,end_port):
    tasks = []
    for port in range(start_port,end_port +1):
        tasks.append(scan_port(ip,port))
    await asyncio.gather(*tasks)

    save_results(ip)

def save_results(ip):
    filename = f"{ip}_scan-results.txt"

    with open(filename,"w") as  f:
        f.write(f"Scan results for{ ip}\n")
        f.write("Open ports:\n")

        for port in sorted(open_ports):
            f.write(f"{port}\n")
    
    print(f"\nResults saved to {filename}")

ip = input("Enter IP:")
start = int(input("Enter start port:"))
end = int(input("Enter end port:"))

asyncio.run(scan(ip,start,end))