import serial
import sys

if __name__ == '__main__':
	port = sys.argv[1]
	s = serial.Serial(port, 9600)
	while True:
		print(s.read())

