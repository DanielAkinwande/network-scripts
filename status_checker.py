import requests

site = input("Enter the website URL to check its status: ")

respond = requests.get(site)
if respond.status_code == 200:
    print(f"The website {site} is up and running!")
else:
    print(f"The website {site} is down. Status code: {respond.status_code}")