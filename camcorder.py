import time
import picamera
import RPi.GPIO as GPIO

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds


camera = picamera.PiCamera()
count = 0

while (1): # run forever
	count += 1
	filename = '/media/usbhdd/video_%d.h264' % count
	camera.start_recording(filename)
	time.sleep(MINUTE) # record for an hour
	camera.stop_recording()

