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
# License: GPL v3 (http://www.gnu.org/licenses/gpl-3.0.txt)
#
# External PiCam resources:
# http://www.raspberrypi.org/documentation/usage/camera/python/README.md
# http://www.raspberrypi.org/learning/python-picamera-setup/
# =====================================================================================
import time
import datetime
import picamera
import RPi.GPIO as GPIO

#LED = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED, GPIO.OUT)

BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

def main():
	with picamera.PiCamera() as camera:
		camera.start_preview()
		camera.resolution = (1920, 1080) # HD resolution

		# Click button to start
		GPIO.wait_for_edge(17, GPIO.FALLING)

		# Create timestamp
		date = datetime.datetime.now()
		camera.led = True
		#GPIO.output(LED, GPIO.HIGH)
		label = date.strftime('%m-%d-%y_%a%b%d_%H%M%S')
		filename = '/media/usbhdd/video_' + label + '.h264'
		print 'recording video clip', label
	
		# Start recording
		camera.start_recording(filename)

		# Click button to stop recording
		GPIO.wait_for_edge(17, GPIO.FALLING)

		# Stop recording
		camera.stop_recording()

if __name__ == "__main__":
	while True:
		main()
