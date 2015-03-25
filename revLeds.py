import getRevs.py
import RPi.GPIO as GPIO
import time

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

while (1 < 2):
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

