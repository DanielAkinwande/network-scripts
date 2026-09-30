import requests
import time
from datetime import datetime
import json
import threading

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sites = ["http://www.google.com", "http://www.github.com", "http://www.stackoverflow.com"]
previous_status = {}
threads = []

def check_site(sites):
        try:
            response = requests.get(site)
            if response.status_code == 200:
                print(f"[{now}] {site} is up and running.")
            else:
                print(f"[{now}] {site} is down. Status code: {response.status_code}")
        except:
            return "Down (No response)"

def monitor(site):
     status = check_site(site)
     print(site, status)

while True:
     time.sleep(10)
     for site in sites:
          t = threading.Thread(target=monitor, args=(site,))
          t.start()
          threads.append(t)

          for t in threads:
              t.join()
          status = check_site(site)
          if site not in previous_status or previous_status[site] != status:
              previous_status[site] = status
              print(f"🚨 ALERT:{site} changed -> {status}")

with open("log.json", "a") as f:
    f.write(json.dumps({"timestamp": now, "site": site, "status": status}) + "\n")

previous_status[site] = status
