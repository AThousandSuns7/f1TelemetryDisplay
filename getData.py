import time
from lxml import html
import requests
import json
import RPi.GPIO as GPIO

#stuff
url = "http://amgwo5:8002/JSON/telemetrypacket" #my system, amgwo5
page = requests.get(url)
print (page.text)

#GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.output(2,False)
GPIO.output(3,False)
GPIO.output(4,False)

lean = 1780.0
standard = 1820.0
full = 1845.0

while True:
	#what actually gets the rev count
	page = requests.get(url)
	decoded = json.loads(page.text)
	revs= decoded['EngineRevs']
	print (revs)
	#if the rev count is greater than lean, less than revs + 13.333, turn on 1
	if (float(revs) >= float(lean)) and (float(revs) < 3000.0):
		GPIO.output(2,True)
	else:
		GPIO.output(2,False)
	if (float(revs) >= float(lean)) and (float(revs) > (float(revs) + 13.333)):
		GPIO.output(3,True)
	if (float(revs) >= float(lean)) and (float(revs) > (float(revs) + 26.666)) #satanwuzhere
		GPIO.output(4,True)
	time.sleep(.1)
