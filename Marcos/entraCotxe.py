# -*- coding: utf-8 -*-
#!/usr/bin/python3


import socket
import sys
import requests
import json
import os
import shutil

hostname = socket.gethostname()
hostname = hostname.strip()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('0.0.0.0', 120)
sock.bind(server_address)

while True:
	print ('\nwaiting to receive message')
	# mat, address = sock.recvfrom(100)
	# mat = bytes(mat).decode("utf-8")
	#Rebem la matricula
	mat = "ABC13"
	if mat:

		body = {"matricula": mat, "parkingID": hostname[-1]}
		request = requests.get('http://10.100.0.1:3002/api/comprovar-reserva-cotxe', data= body)
		reserva = request.json()
		print(reserva['status'])

		#Comprovem status de la reserva
		if(reserva['status'] == 0):
			sPath = "/root/matriculasComprovar/"
			end = ".txt"
			dPath = "/root/matriculasValidas/"
			sPath = sPath + str(mat) + end
			dPath = dPath + str(mat) + end
			os.system('touch {}'.format(sPath))
			os.rename(sPath, dPath)

			# Preguntem la plaça disponible
			request2 =  requests.post('http://10.100.0.1:3002/api/introduir-cotxe-parking', data = body)
			plaza = request2.json()

			print (body)
			print(plaza['status'])
			print(plaza['plazaID'])


			#Enviem OK a l'entrada del cotxe amb la plaça
			#res = "0,"+str(plaza['plazaID'])
			#sent = sock.sendto(bytes(res.encode("utf-8")), ('10.90.0.18',120))

		else:
			#Informem que no pot passar a la barrera
			#res = "1,9"
			# sent = sock.sendto(bytes(res.encode("utf-8")), ('10.90.0.18',120))

			print("El cotxe no té reserva. No pot entrar")
