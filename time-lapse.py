import time
import picamera
import RPi.GPIO as GPIO

DELAY = 10 # time between frame in seconds

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

camera = picamera.PiCamera()
count = 0

while (1): # run forever
	count += 1
	filename = '/media/usbhdd/img_%d.h264' % count
	camera.capture(filename)
	time.sleep(DELAY) # capture every DELAY seconds

