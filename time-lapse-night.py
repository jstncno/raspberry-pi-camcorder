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
import weather

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

DELAY = 10 # time between frame in seconds

camera = picamera.PiCamera()
camera.resolution = (2592, 1944) # HD resolution

LED = 17
GPIO.setmode(BCM)
GPIO.setup(LED, GPIO.OUT)

SUNRISE = weather.SUNRISE
SUNSET = weather.SUNSET
SUNRISE_HOUR, SUNRISE_MINUTE = weather.parseTimestamp(SUNRISE)
SUNSET_HOUR, SUNSET_MINUTE = weather.parseTimestamp(SUNSET)

# <ON_HOUR:ON_MINUTE> = the time for the camera to turn on
# Turns on an hour before sunset
ON_HOUR = SUNSET_HOUR - 1
ON_MINUTE = SUNSET_MINUTE

# <OFF_HOUR:OFF_MINUTE> = the time for the camera to turn off
# Turns off an hour after sunrise
OFF_HOUR = SUNRISE_HOUR + 1
OFF_MINUTE = SUNRISE_MINUTE

def nighttime(current_hour, current_minute):
	if current_hour == ON_HOUR:
		return current_minute >= ON_MINUTE
	if current_hour == OFF_HOUR:
		return current_minute < OFF_MINUTE
	
	return current_hour < OFF_HOUR or ON_HOUR < current_hour

def main():
	date = datetime.datetime.now()
	current_hour = int(date.strftime('%H'))
	current_minute = int(date.strftime('%M'))
	if nighttime(current_hour, current_minute):
		camera.led = True
		GPIO.output(LED, GPIO.HIGH)
		label = date.strftime('%m-%d-%y_%a%b%d_%H%M%S')
		filename = '/media/usbhdd/img_' + label + '.jpg'
		print 'capturing image', label
		camera.start_capture(filename)
		time.sleep(DELAY) # delay before next picture
	else:
		GPIO.outpu(LED, GPIO.LOW)
		camera.led = False
		time.sleep(MINUTE)

if __name__ == "__main__":
	while True:
		main()
