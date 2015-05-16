import serial
import time
import datetime

while True:
	myfile=open("temperatura.txt","a")
	ser = serial.Serial('/dev/ttyACM0',9600)
	strLinha = ser.readline()
	ser.close()
	strLinha = datetime.datetime.today().strftime("%d/%m/%y - %H:%M:%S - ") + strLinha
	myfile.write(strLinha)
	myfile.close()
	time.sleep(5)
