import quote
from ctypes import windll
from os.path import dirname, abspath
from requests import get

from SimpleUpdater import SimpleUpdater

CURRENT_VERSION = '0.0.1'
VERSION_URL = 'https://raw.githubusercontent.com/mvishok/InspireWall/main/ver.txt'
SimpleUpdater.checkForUpdates(CURRENT_VERSION, VERSION_URL)

resp = get("https://api.quotable.io/random").json()
content = resp['content'] + " - " + resp['author']
quote.save(content, 612, 612)
p = dirname(abspath(__file__))+'\quote.png'
windll.user32.SystemParametersInfoW(20, 0, p, 3)
