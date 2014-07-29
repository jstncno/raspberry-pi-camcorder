#!/usr/bin/python
import time
import datetime
import RPi.GPIO as GPIO

DEBUG = 1
SENSOR = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.OUT)

def getLightReading():
	reading = 0
	GPIO.setup(SENSOR, GPIO.OUT)
	GPIO.output(SENSOR, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(SENSOR, GPIO.IN)

	while GPIO.input(SENSOR) == (GPIO.LOW):
		reading += 1
	return reading

if __name__ == "__main__":
	while True:
		date = datetime.datetime.now().strftime("%X")
		print "[" + str(date) + "] " + str(getLightReading())
		time.sleep(1)
