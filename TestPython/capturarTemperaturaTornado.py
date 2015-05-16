import time
import serial
import datetime
from websocket_messaging import websocket_send
 
# Iniciando conexao serial
comport = serial.Serial('/dev/ttyACM0', 9600)

while True: 
	# Time entre a conexao serial e o tempo para escrever (enviar algo)
	time.sleep(1.8) # Entre 1.5s a 2s
 
	VALUE_SERIAL=comport.readline()
 	websocket_send('http://127.0.0.1:8888', datetime.datetime.today().strftime("%d/%m/%y %H:%M:%S ") + '%s' % (VALUE_SERIAL), 'mykey', 'mygroup')
 
# Fechando conexao serial
comport.close()
