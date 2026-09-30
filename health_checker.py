import requests
import socket

def check_http(url):
    try:
        requests.get(url, timeout=5)
        return "UP"
    except:
        return "DOWN"

def check_port(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return "UP"
    except:
        return "DOWN"

def run_checks():
    return [
        {"name": "Google", "status": check_http("https://google.com")},
        {"name": "Local SSH", "status": check_port("127.0.0.1", 22)}
    ]