# ===================================================================================== 
# camcorder.py
# =====================================================================================    
# Copyright 2014 Justin Cano
# http://www.justincano.com
#
# Python script to record video clips to an external mounted USB NTFS hard drive.
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
import light
import time
import datetime
import picamera
import RPi.GPIO as GPIO

# The threshold value to determine when to turn on the camera. Range:
# 1(light) ~ 50,000(dark)
LIGHT_THRESHOLD = 15000

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

RECORDING_LENGTH = HOUR # 3600 seconds

camera = picamera.PiCamera()
camera.resolution = (1920, 1080) # HD resolution

LED = 17 # GPIO pin

GPIO.setmode(GPIO.BCM)

while (1): # run forever
	reading = light.getLightReading()
	if reading > LIGHT_THRESHOLD:
		date = datetime.datetime.now().strftime('%m-%d-%y_%a%b%d_%H%M%S')
		filename = '/media/usbhdd/video_' + date + '.h264'
		print 'recording video clip', date
		camera.start_recording(filename)
		time.sleep(HOUR) # record for an hour
		camera.stop_recording()

