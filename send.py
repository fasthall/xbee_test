import serial
import sys

if __name__ == '__main__':
	port = sys.argv[1]
	msg = sys.argv[2]
	s = serial.Serial(port, 9600)
	s.write(list(bytearray(msg, 'utf-8')))
