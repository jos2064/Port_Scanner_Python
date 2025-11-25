# Python Port Scanners – 8 Different Implementations

This repository contains eight progressively advanced port scanners, each demonstrating different networking, threading, asynchronous, and service-identification techniques in Python.

These scripts show the evolution from basic socket programming to multi-threaded, thread-pool, banner identification, and high-speed asynchronous scanning.
Included Scanners (8 Versions)
# 1. Basic Port Scanner

Single-port scan using plain sockets

Perfect starting point for learning network programming

# 2.Port Scanner with For Loop

Scans multiple ports sequentially

Teaches iteration + socket handling

# 3.Multi-threaded Port Scanner

Uses threading.Thread

Great speed improvement

Good introduction to concurrency

# 4.Thread-Pool Port Scanner (Executor)

(Moved below threading as you requested)

Uses concurrent.futures.ThreadPoolExecutor

Cleaner and more controlled threading

Faster + safer compared to raw threads

# 5.Banner-Only Fetcher

(Moved above banner-grabbing scanner)

Connects to a port

Grabs whatever banner the service sends

Useful to identify running services

# 6.Port Scanner + Banner Grabbing

Scans ports

For every open port → grabs banner

Helps fingerprint services like FTP, SSH, HTTP, SMTP

# 7. Async Port Scanner

Uses asyncio

Massive speed boost through non-blocking I/O

Great for scanning large port ranges

# 8. Async Port Scanner with Banner Grab

Fully asynchronous

Extremely fast

Reads banners via async streams

Best performance out of all versions

# To run these codes individually
-> Go to your cmd
-> type- python filename.py 
           OR
         python3 filename.py
