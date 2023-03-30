import quote
from ctypes import windll
from os.path import dirname, abspath
import updater

resp = updater.get("https://api.quotable.io/random").json()
content = resp['content'] + " - " + resp['author']
quote.save(content, 612, 612)
p = dirname(abspath(__file__))+'\quote.png'
windll.user32.SystemParametersInfoW(20, 0, p, 3)
