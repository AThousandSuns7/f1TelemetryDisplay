import time
from lxml import html
import requests
import json

#stuff
url = "http://amgwo5:8002/JSON/telemetrypacket" #my system, amgwo5
page = requests.get(url)
print (page.text)

while True:
	#what actually gets the rev count
	page = requests.get(url)
	decoded = json.loads(page.text)
	revs= decoded['EngineRevs']
	print (revs)
	time.sleep(.5)
