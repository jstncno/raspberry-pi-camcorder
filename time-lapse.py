# time-lapse.py
#
# Python script to capture time-lapse images to an external mounted USB NTFS hard drive.
# Use time.sleep() for delay between frames
# 
# External PiCam resources:
# http://www.raspberrypi.org/documentation/usage/camera/python/README.md
# http://www.raspberrypi.org/learning/python-picamera-setup/import time
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
	print 'capturing image', count
	filename = '/media/usbhdd/img_%d.jpg' % count
	camera.capture(filename)
	time.sleep(DELAY) # capture every DELAY seconds

