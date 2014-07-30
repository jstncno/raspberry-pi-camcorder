# ===================================================================================== 
# camcorder-day.py
# =====================================================================================    
# Copyright 2014 Justin Cano
# http://www.justincano.com
#
# Python script to record video clips to an external mounted USB NTFS hard drive.
# This script is intended to operate the camera at DAY TIME hours, after sunrise and
# before sunset.
# Use time.sleep() record for desired amount of time
#
# Video files saved as .h264 named by their timestamp
# Filename: video_<month>-<day>-<year>_<weekday><day>_<hour><min><sec>.h264
# Format: MM-DD-YY_DayDD_hhmmss
# Example: 06-27-14_Thurs27_221834 => Thursday, June 27 2014 at 10:18pm
#
# License: GPL v3
#
# External PiCam resources:
# http://www.raspberrypi.org/documentation/usage/camera/python/README.md
# http://www.raspberrypi.org/learning/python-picamera-setup/
# =====================================================================================
import time
import datetime
import picamera
import RPi.GPIO as GPIO
import sun

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

DELAY = 10 # time between frame in seconds

camera = picamera.PiCamera()
camera.resolution = (2592, 1944) # HD resolution

def main():
	date = datetime.datetime.now()
	current_day = int(date.strftime('%d'))
	current_date = str(current_day) + date.strftime('-%b')
	current_time = int(date.strftime('%H%M'))
	if sun.daytime(current_date, current_time):
		camera.led = True
		label = date.strftime('%m-%d-%y_%a%b%d_%H%M%S')
		filename = '/media/usbhdd/img_' + label + '.jpg'
		print 'capturing image', label
		camera.capture(filename)
		time.sleep(DELAY) # delay before next picture
	else:
		camera.led = False
		time.sleep(MINUTE)

if __name__ == "__main__":
	while True:
		main()
