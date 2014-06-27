# camcorder.py
#
# Python script to record video clips to an external mounted USB NTFS hard drive.
# Use time.sleep() record for desired amount of time
#
# Video files saved as .h264 named by their timestamp
# Filename: video_<month>-<day>-<year>_<weekday><day>_<hour><min><sec>.h264
# Format: MM-DD-YY_DayDD_hhmmss
# Example: 06-27-14_Thurs27_221834 => Thursday, June 27 2014 at 10:18pm
#
# External PiCam resources:
# http://www.raspberrypi.org/documentation/usage/camera/python/README.md
# http://www.raspberrypi.org/learning/python-picamera-setup/
import time
import datetime
import picamera
import RPi.GPIO as GPIO

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

camera = picamera.PiCamera()

while (1): # run forever
	date = datetime.datetime.now().strftime('%m-%d-%y_%a%b%d_%H%M%S')
	filename = '/media/usbhdd/video_' + date + '.h264'
	print 'recording video clip', date
	camera.start_recording(filename)
	time.sleep(HOUR) # record for an hour
	camera.stop_recording()

