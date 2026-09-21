import socket

ports = range(20, 100)
target = socket.gethostbyname(socket.gethostname())

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(target, ports)
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")