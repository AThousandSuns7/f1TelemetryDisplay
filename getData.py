import time
from lxml import html
import requests
import json
import RPi.GPIO as GPIO

#stuff
url = "http://amgwo5:8002/JSON/telemetrypacket" #my system, amgwo5
page = requests.get(url)
print (page.text)

#what actually gets the rev count
while True:
	page = requests.get(url)
	decoded = json.loads(page.text)
	revs= decoded['EngineRevs']
	print (revs)
	time.sleep(.1)

#GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

lean = 1780.0
standard = 1820.0
full = 1845.0

#if the rev count is greater than lean, less than revs + 13.333, turn on 1
if (revs >= lean) and (revs < 3000.0)
	GPIO.output(14,True)
	else GPIO.output(14,False)
	
if (revs >= lean) and (revs > (revs + 13.333))
	GPIO.output(15,True)

if (revs >= lean) and (revs > (revs + 26.666)) #satanwuzhere
	GPIO.output(18,True)
	
