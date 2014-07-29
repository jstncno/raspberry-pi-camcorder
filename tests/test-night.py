import light
import time
import RPi.GPIO as GPIO

LIGHT_THRESHOLD = 1000

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

while True:
	reading = light.getLightReading()
	if reading >= LIGHT_THRESHOLD:
		GPIO.output(LED, GPIO.HIGH)
	else:
		GPIO.output(LED, GPIO.LOW)
