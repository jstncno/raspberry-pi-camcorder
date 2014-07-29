import serial
import time
import light
ser = serial.Serial('/dev/ttyAMA0', 9600)

while True:
	data = str(light.getLightReading())
	ser.write(data)
	print data
	time.sleep(3)
