# -*- coding: utf-8 -*-
#!/usr/bin/python3


import socket
import sys
import requests
import json
import os
import shutil

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.43.67', 120)
sock.bind(server_address)

while True:
	print ('\nwaiting to receive message')
	mat, address = sock.recvfrom(100)
	mat = bytes(mat).decode("utf-8")
	#Rebem la matricula
	if mat:
		body = {"matricula": mat, "parkingID": 1}
		request = requests.get('http://craaxcloud.epsevg.upc.edu:19002/api/comprovar-reserva-coche', data= body)
		reserva = request.json()
		print(reserva['status'])
		request2 =  requests.post('http://craaxcloud.epsevg.upc.edu:19002/api/introduir-coche-parking', data = body)
		plaza = request2.json()
		print(plaza['plazaID'])

		#Enviem OK a l'entrada del cotxe
		res = reserva['status'] + "," + plaza['plazaID']
		sent = sock.sendto(bytes(res, "utf-8"), ('192.168.43.63',120))

		if(reserva['status'] == 0):
			sPath = "/root/matriculasComprovar/"
			dPath = "/root/matriculasValidas/"
			end = ".txt"
			sPath = sPath + mat + end
			dPath = dPath + mat + end
			os.rename(sPath, dPath)

		else:
			print("El cotxe no té reserva. No pot entrar")
