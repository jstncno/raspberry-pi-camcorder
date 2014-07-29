import serial
import time
import light
ser = serial.Serial('/dev/ttyAMA0', 9600)

while True:
	data = ser.readline()
	print data
