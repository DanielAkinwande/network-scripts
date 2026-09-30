import requests


sites = ["http://www.google.com", "http://www.github.com", "http://www.stackoverflow.com"]

for site in sites:
    try:
        respond = requests.get(site)
        if respond.status_code == 200:
            print(f"The website {site} is up and running!")
        else:
            print(f"The website {site} is down. Status code: {respond.status_code}")
    except requests.RequestException as e:
        print(f"Error occurred while checking {site}: {e}")