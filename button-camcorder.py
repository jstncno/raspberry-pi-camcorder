# ===================================================================================== 
# camcorder-night.py
# =====================================================================================    
# Copyright 2014 Justin Cano
# http://www.jcano.me
#
# Python script to record video clips to an external mounted USB NTFS hard drive.
# This script is intended to operate the camera using a button mechanism that acts as a
# switch.
# Click button to begin recording, click again to stop.
#
# Video files saved as .h264 named by their timestamp
# Filename: video_<month>-<day>-<year>_<weekday><day>_<hour><min><sec>.h264
# Format: MM-DD-YY_DayDD_hhmmss
# Example: 06-27-14_Thurs27_221834 => Thursday, June 27 2014 at 10:18pm
#
# License: GPL v3 (http://www.gnu.org/licenses/gpl-3.0.txt)
#
# External PiCam resources:
# http://www.raspberrypi.org/documentation/usage/camera/python/README.md
# http://www.raspberrypi.org/learning/python-picamera-setup/
# http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
# =====================================================================================
import time
import datetime
import sys
import picamera
import RPi.GPIO as GPIO

HOUR = 3600 # in seconds

# Setup camera
camera = picamera.PiCamera()
camera.resolution = (1920, 1080) # HD resolution

#LED = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED, GPIO.OUT)

BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, GPIO.PUD_UP)

def stopRecording(channel):
	print "Stopping recording..."
	camera.stop_recording()
	camera.stop_preview()
	print "Recording stopped."
	sys.exit()

GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=stopRecording, bouncetime=300)

def main():
	# Create timestamp
	date = datetime.datetime.now()
	#GPIO.output(LED, GPIO.HIGH)
	label = date.strftime('%m-%d-%y_%a%b%d_%H%M%S')
	filename = '/media/usbhdd/video_' + label + '.h264'
	print 'recording video clip', label

	# Start recording
	camera.start_preview()
	camera.start_recording(filename)
	camera.led = True

	# Record for an hour
	time.sleep(HOUR)

	# Stop recording
	camera.stop_recording()
	camera.stop_preview()
	

if __name__ == "__main__":
	while True:
		main()
