#!/usr/bin/python
import time, os, subprocess, re, shutil, requests, json


def primeraIPDisponible():
	for x in os.listdir('/root/matriculasValidas'):
		# Registramos la direccion del archivo para poder abrirlo
		aux2 = "/root/matriculasValidas/" + str(x)
		with open (aux2) as origin_file:
			#Vamos leyendo linea por linea
			for i,line in enumerate(origin_file):
				if i == 3:
				    matricula = line.rstrip("\n")
				   # Buscamos si hay "IP" en la linea
				if 'IP' in line:
					IP = line.split()[2]
					body = {"matricula":matricula}
					r = requests.get('http://10.100.0.1:3002/api/comprovar-estat-cotxe', data = body)
					print(r.status_code)
					get_json = r.json()
					print(get_json)
					print(get_json.get('estat_coche'))
					if(get_json.get('estat_coche') == 1):
						return IP, matricula
					else: break

	#Si el codigo llega aqui, significa que no ha encontrado ninguna IP con estado disponible. Tendriamos que devolver algo para que lo vuelva a intentar en x segundos.
	print("No entra")
	return "noIP","NONE"

# Ponemos while 1 pq se ejecuta todo el rato, pararemos cuando arranque el coche, ja que para toda la computacion
while 1:
	# Si hay algun archivo
	for x in os.listdir('/root/toExecute'):
		IP, matricula = primeraIPDisponible()
		while IP == "noIP":
			time.sleep(5)
			IP, matricula = primeraIPDisponible()

		print(IP)
		print(matricula)
		dir_programa = "/root/toExecute/" + str(x)
		#Hacemos el SCP
		p = subprocess.Popen (["scp", dir_programa, "root@"+IP+":/root/comp"])
		# Esperamos a que termine el envio.
		sts = os.waitpid(p.pid, 0)

		# Actualización del estado del coche en la API
		body = {"matricula":matricula, "estado_coche":2}
		req = requests.post('http://10.100.0.1:3002/api/actualitzar-estat-cotxe', data = body)
		print(req.status_code)
		getjson = req.json()
		print(getjson)

		#Ahora que el programa ya se ha mandado al agente en cuestion, lo eliminamos del server.
		#os.remove(dir_programa)

	# Pongo un sleep de cinco para no se satura el ordenador
	time.sleep(5)
