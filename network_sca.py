import subprocess
import time
import socket
from datetime import datetime

known_devices = set()
ip = socket.gethostbyname(socket.gethostname())
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

 
while True:
    #scan logic here
    time.sleep(10)  # Wait for 10 seconds before scanning again
    result = subprocess.check_output("arp -a", shell=True)
    text = result.decode("utf-8")
    line = text.splitlines(".")


    current_devices = set()
    for l in line:
        if "." in l:
            current_devices.add(l.split()[0])

    new_devices = current_devices - known_devices



    known_devices = current_devices

    def scan_ports():
        ports = range(20, 100)
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((ip, port))
        if result == 0:
            return f"Port {port} is open"
        else:
            return f"Port {port} is closed"
        s.close()

    for device in new_devices:
        print(f"🚨 NEW DEVICE: {device} at {now}")
        scan_ports() 

    with open("network_history.txt", "a") as f:
        f.write(f"[{now}] NOW [{device}]\n")
 