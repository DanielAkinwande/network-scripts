import requests
import socket
import time
from datetime import datetime

now = datetime.now()

def check_http(url):
    try:
        start_time = time.time()
        requests.get(url, timeout=5)
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convert to milliseconds
        return f"{now.strftime('%Y-%m-%d %H:%M:%S')} - UP ({latency:.2f}ms)"
    except:
        return f"{now.strftime('%Y-%m-%d %H:%M:%S')} - DOWN"

def check_port(host, port):
    try:
        start_time = time.time()
        socket.create_connection((host, port), timeout=5)
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convert to milliseconds

        return f"{now.strftime('%Y-%m-%d %H:%M:%S')} - UP ({latency:.2f}ms)    "
    except:
        return f"{now.strftime('%Y-%m-%d %H:%M:%S')} - DOWN"

def run_checks():
    return [
        {"name": "Google", "status": check_http("https://google.com")},
        {"name": "Local SSH", "status": check_port("127.0.0.1", 22)}
    ]