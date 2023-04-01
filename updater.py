from pymsgbox import confirm, alert
from requests import get
from webbrowser import open

res = get('https://api.github.com/repos/mvishok/InspireWall/releases/latest')
if res.status_code == 200:
    latest = res.json()['tag_name']
    if latest != 'v1.0.0':
        if confirm(f"New version ({latest}) of InspireWall is available. Download?", "InspireWall") == "OK":
            open(res.json()['html_url'])
else:
    alert("Unable to fetch latest release info.", "InspireWall")
