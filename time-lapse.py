# time-lapse.py
#
# Python script to capture time-lapse images to an external mounted USB NTFS hard drive.
# Use time.sleep() for delay between frames
# 
# Image files saved as .jpg named by their timestamp
# Filename: img_<month>-<day>-<year>_<weekday><day>_<hour><min><sec>.jpg
# Format: MM-DD-YY_DayDD_hhmmss
# Example: 06-27-14_Thurs27_221834 => Thursday, June 27 2014 at 10:18pm
#
# External PiCam resources:
# http://www.raspberrypi.org/documentation/usage/camera/python/README.md
# http://www.raspberrypi.org/learning/python-picamera-setup/import time
import time
import datetime
import picamera
import RPi.GPIO as GPIO

DELAY = 10 # time between frame in seconds

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

camera = picamera.PiCamera()

while (1): # run forever
	date = datetime.datetime.now().strftime('%m-%d-%y_%a%b%d_%H%M%S')
	filename = '/media/usbhdd/img_' + date + '.jpg'
	print 'capturing image', date
	camera.capture(filename)
	time.sleep(DELAY) # capture every DELAY seconds
