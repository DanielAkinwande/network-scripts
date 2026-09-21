import os

ip = input("Enter the IP address to ping: ")
response = os.system(f"ping -c 4 {ip}")
if response == 0:
    print(f"{ip} is reachable.")
else:
    print(f"{ip} is not reachable.")