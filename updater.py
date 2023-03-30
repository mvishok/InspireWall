from requests import get

def check_updates():
    res = get('https://api.github.com/repos/mvishok/InspireScreen/releases/latest')
    if res.status_code == 200:
        latest = res.json()['tag_name']
        if latest != 'v1.0.0':
            print(f"New version ({latest}) available at {res.json()['html_url']}.")
        else:
            print("You're running the latest version.")
    else:
        print("Unable to fetch latest release info.")
