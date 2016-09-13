import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.timeout = 1

ser.open()
ser.flushInput()
ser.flushOutput()
st = str()
print(ser.name)
print(ser.port)

while True:
	time.sleep(0.1)
	iw = ser.in_waiting
	if not iw == 0:
		byte = ser.read(iw)
		tx = byte.decode('utf-8')
		if tx[-1] == '\r':
			print(st,end=None)
			st = ''
		else:
			st += tx
		
	
		
	
		

