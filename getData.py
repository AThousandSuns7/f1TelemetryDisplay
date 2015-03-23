import time
from lxml import html
import requests
import json

url = "http://localhost:8002/JSON/telemetrypacket"
page = requests.get(url)
print (page.text)

while True:
	page = requests.get(url)
	decoded = json.loads(page.text)
	revs= decoded['EngineRevs']
	print (revs)
	time.sleep(.1)
	
	
	1824.10
	1808.63
	1838.38
	