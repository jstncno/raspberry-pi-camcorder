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
import time
import datetime
import picamera
import RPi.GPIO as GPIO
import weather

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

RECORDING_LENGTH = HOUR # 3600 seconds

#camera = picamera.PiCamera()
#camera.resolution = (1920, 1080) # HD resolution

SUNRISE = weather.SUNRISE
SUNSET = weather.SUNSET

#def turnOnLED():
#	camera.led = True

#def turnOffLED():
#	camera.led = False

def main():
	date = datetime.datetime.now()
	label = date.strftime('%m-%d-%y_%a%b%d_%H%M%S')
	filename = '/media/usbhdd/video_' + label + '.h264'
	sunrise_hour, sunrise_min = weather.parseTimestamp(SUNRISE)
	print sunrise_hour, sunrise_min
	time.sleep(10)
#	print 'recording video clip', date
#	camera.start_recording(filename)
#	time.sleep(HOUR) # record for an hour
#	camera.stop_recording()

if __name__ == "__main__":
	while True:
		main()
