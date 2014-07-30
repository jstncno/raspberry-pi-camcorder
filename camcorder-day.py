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
import pywapi

ZIP = "92507"

MINUTE = 60 # in seconds
HOUR = 3600 # in seconds

RECORDING_LENGTH = HOUR # 3600 seconds

#camera = picamera.PiCamera()
#camera.resolution = (1920, 1080) # HD resolution

''' Get weather from different weather stations '''
yahoo_weather = pywapi.get_weather_from_yahoo(ZIP)
weather_com_weather = pywapi.get_weather_from_weather_com(ZIP)

sunrise = open('SUNRISE.txt', 'w+')
sunset = open('SUNSET.txt', 'w+')
if 'astronomy' in yahoo_weather:
	if 'sunrise' in yahoo_weather['astronomy']:
		sunrise.write(str(yahoo_weather['astronomy']['sunrise']))
	if 'sunset' in yahoo_weather['astronomy']:
		sunset.write(str(yahoo_weather['astronomy']['sunset']))


elif 'forecasts' in weather_com_weather:
	sunrise.write(str(weather_com_weather['forecasts'][0]['sunrise']))
	sunset.write(str(weather_com_weather['forecasts'][0]['sunset']))
sunrise.close()
sunset.close()

#def turnOnLED():
#	camera.led = True

#def turnOffLED():
#	camera.led = False

while (1): # run forever
#	turnOnLED()
	date = datetime.datetime.now().strftime('%m-%d-%y_%a%b%d_%H%M%S')
	filename = '/media/usbhdd/video_' + date + '.h264'
	print 'recording video clip', date
#	camera.start_recording(filename)
	time.sleep(HOUR) # record for an hour
#	camera.stop_recording()
#	turnOffLED()
