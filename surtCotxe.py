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

server_address = ('192.168.43.159', 120)
sock.bind(server_address)

while True:

	try:
		print ('\nwaiting to receive message')
		data, address = sock.recvfrom(100)
		data = bytes(data).decode("utf-8")
		mat = data.split(",")[1]
		qr = data.split(",")[0]
	except:
		print("Connexió amb sockets ha fallat")

	if mat:
		try:
			body = {"matricula": mat, "qr": qr}
			request = requests.post('http://10.100.0.1:3002/api/sortida-cotxe-parking', data= body)
			sortir = request.json()
			print("status de sortida")
			n = sortir['status']

			print(n)
			res = str(n)
			sent = sock.sendto(bytes(res.encode("utf-8")), ('192.168.43.76',120))
		except:
			print("Connexió amb barrera incorrecta sortida parquing")

		if res == n:


			try:
				body = ("matricula":mat)
				request = requests.get('http://10.100.0.1:3002/api/comprovar-estat-cotxe', data = body)
				print("Comprovar estat cotxe")
				#status = request.json()
				#print(status['status'])
				print(request.status_code)
				if request.json['estado_coche'] == 2:
					body = {"matricula":mat,"estado_coche":"1"}
					request = requests.post('http://10.100.0.1:3002/api/actualitzar-estat-cotxe', data = body)
					print(request.status_code)


			dPath = "/root/matriculasValidas/"
			end = ".txt"
			dPath = dPath + str(mat) + end
			os.remove(dPath)
			print("matricula eliminada del parquing")
