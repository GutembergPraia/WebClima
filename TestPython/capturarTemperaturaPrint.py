import time
import serial
import datetime
 
# Iniciando conexao serial
comport = serial.Serial('/dev/ttyACM0', 9600)

while True: 
	# Time entre a conexao serial e o tempo para escrever (enviar algo)
	time.sleep(1.8) # Entre 1.5s a 2s
 
	VALUE_SERIAL=comport.readline()
 	print datetime.datetime.today().strftime("%d/%m/%y - %H:%M:%S - ") + '%s' % (VALUE_SERIAL)
 
# Fechando conexao serial
comport.close()
