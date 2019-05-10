# -*- coding: utf-8 -*-
#!/usr/bin/python3


import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.43.67', 120)
sock.bind(server_address)

while True:
	print ('\nwaiting to receive message')
	data, address = sock.recvfrom(100)
	data = bytes(data).decode("utf-8")
	#Rebem la matricula
	print (data)

	#Falta comprovar l'existencia de l'usuari i si està registrat
	if data:
		#Enviem OK a l'entrada del cotxe
		sent = sock.sendto(bytes('OK',"utf-8"), ('192.168.43.63',120))
