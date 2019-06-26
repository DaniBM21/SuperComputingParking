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

	try:
		print ('\nwaiting to receive message')
		data, address = sock.recvfrom(100)
		data = bytes(data).decode("utf-8")
		if data:
			mat = data.split(",")[1]
			qr = data.split(",")[0]
	except:
		print("Connexió amb sockets ha fallat")

	if mat and qr:
		i = 0
		try:
			while i < 3:
				body = {"matricula": mat, "qr": qr}
				request = requests.post('http://10.100.0.1:3002/api/sortida-cotxe-parking', data= body)
				sortir = request.json()
				if request.status_code == 200 and str(sortir['status']) == "1":
					n = sortir['status']
					m = sortir['message']
					res = str(n) + "," + str(m)
					print(res)
					sent = sock.sendto(bytes(res.encode("utf-8")), ('192.168.43.76',120))
					i = 3
				elif request.status_code == 200:
					n = sortir['status']
					m = "El cotxe pot sortir"
					res = str(n) + "," + str(m)
					print(res)
					sent = sock.sendto(bytes(res.encode("utf-8")), ('192.168.43.76',120))
					i = 3

					try:
						j = 0
						while j < 3:
							body = ("matricula":mat)
							request = requests.get('http://10.100.0.1:3002/api/comprovar-estat-cotxe', data = body)
							print("Comprovar estat cotxe")
							estat = request.json()
							if request.status_code == 200 and str(estat['status']) == "0":
								if str(estat['estat_coche']) == "2":

									body = {"matricula":mat,"estado_coche":"1"}
									request = requests.post('http://10.100.0.1:3002/api/actualitzar-estat-cotxe', data = body)
									act = request.json()
									if request.status_code == 200 and str(act['status']) == "0":
										j = 3
										dPath = "/root/matriculasValidas/"
										end = ".txt"
										dPath = dPath + str(mat) + end
										os.remove(dPath)
										print("matricula eliminada del parquing")

							else:
								j = j+1


					except:
						print("Han fallat les consultes d'estat")

				else:
					i = i+1

		except:
			print("Consultes a la api no han funcionat")

