# -*- coding: utf-8 -*-
#!/usr/bin/python3


import socket
import sys
import requests
import json
import os
import shutil


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('0.0.0.0', 120)
sock.bind(server_address)
while 1:
	try:
		print ('\nwaiting to receive message')
		data, address = sock.recvfrom(500)
		data = bytes(data).decode("utf-8")
		print (data)
		if data:
			mat = data.split(",")[1]
			qr = data.split(",")[0]

			print(qr)
			print(mat)
	except:
		print("Connexió amb sockets ha fallat")

	if data and mat and qr:
		i = 0
		if 1:
			while i < 3:
				body = {"matricula": mat, "qr": qr}
				#request = requests.post('http://craaxcloud.epsevg.upc.edu:19022/api/sortida-cotxe-parking', data = body)
				request = requests.post('https://10.100.0.1:3002/api/sortida-cotxe-parking', data= body, verify=False)
				sortir = request.json()
				print("Status_code")
				print(request.status_code)
				print("Status")
				print(sortir['status'])

				if str(request.status_code) == "200" and str(sortir['status']) == "1":
					n = sortir['status']
					m = sortir['message']
					print("Ha entrat on toca")
					print(n)
					print(m)
					res =  str(n) + "," +  str(m)
					print(res)
					sent = sock.sendto(bytes(res.encode("utf-8")), ('10.90.0.18',120))
					i = 3
				elif str(request.status_code) == "200":
					print("elif")
					n = sortir['status']
					m = sortir['import']
					res = str(n) + "," + "Has pagat: " + str(m)
					print(res)
					sent = sock.sendto(bytes(res.encode("utf-8")), ('10.90.0.18',120))
					i = 3

					try:
						j = 0
						while j < 3:
							body = {"matricula":mat}
							request = requests.get('https://10.100.0.1:3002/api/comprovar-estat-cotxe', data = body,verify=False)
							print("Comprovar estat cotxe")
							estat = request.json()
							if request.status_code == "200" and str(estat['status']) == "0":
								if str(estat['estat_coche']) == "2":

									body = {"matricula":mat,"estado_coche":"1"}
									request = requests.post('http://10.100.0.1:3002/api/actualitzar-estat-cotxe', data = body)
									act = request.json()
									if request.status_code == "200" and str(act['status']) == "0":
										j = 3
										dPath = "/root/matriculasValidas/"
										end = ".txt"
										dPath = dPath + str(mat) + end
										os.remove(dPath)
										print("matricula eliminada del parquing")
									else:
										j = j+1
							else:
								j = j+1


					except:
						print("Han fallat les consultes d'estat")

				else:
					print("Ha entrat al else")
					i = i+1

		else:
			print("Consultes a la api no han funcionat")

