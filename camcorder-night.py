# ===================================================================================== 
# camcorder-night.py
# =====================================================================================    
# Copyright 2014 Justin Cano
# http://www.justincano.com
#
# Python script to record video clips to an external mounted USB NTFS hard drive.
# This script is intended to operate the camera at NIGHT TIME hours, before sunrise and
# after sunset.
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

RECORDING_LENGTH = HOUR # 3600 seconds

camera = picamera.PiCamera()
camera.resolution = (1920, 1080) # HD resolution

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def main():
	date = datetime.datetime.now()
	if sun.nighttime(date):
		camera.led = True
		GPIO.output(LED, GPIO.HIGH)
		label = date.strftime('%m-%d-%y_%a%b%d_%H%M%S')
		filename = '/media/usbhdd/video_' + label + '.h264'
		print 'recording video clip', label
		camera.start_recording(filename)
		time.sleep(HOUR) # record for an hour
		camera.stop_recording()
	else:
		GPIO.output(LED, GPIO.LOW)
		camera.led = False
		time.sleep(MINUTE)

if __name__ == "__main__":
	while True:
		main()
