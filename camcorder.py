# camcorder.py
#
# Python script to record video clips to an external mounted USB NTFS hard drive.
# Use time.sleep() record for desired amount of time
#
# External PiCam resources:
# http://www.raspberrypi.org/documentation/usage/camera/python/README.md
# http://www.raspberrypi.org/learning/python-picamera-setup/
import time
import picamera
import RPi.GPIO as GPIO

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

camera = picamera.PiCamera()
count = 0

while (1): # run forever
	count += 1
	print "recording video", count
	filename = '/media/usbhdd/video_%d.h264' % count
	camera.start_recording(filename)
	time.sleep(HOUR) # record for an hour
	camera.stop_recording()

