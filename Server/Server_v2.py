#!/usr/bin/python
import time, os, subprocess, re, shutil, requests, json

matricula = "A"

def primeraIPDisponible():
	print("Entra funcion")
	for x in os.listdir('/root/matriculasValidas'):
		# Registramos la direccion del archivo para poder abrirlo
		aux2 = "/root/matriculasValidas/" + str(x)
		print(aux2)
		with open (aux2) as origin_file:
			#Vamos leyendo linea por linea
			for i,line in enumerate(origin_file):
				if i == 3:
				      	matricula = line.rstrip("\n")

				# Buscamos si hay "IP" en la linea
				if 'IP' in line:
					print (matricula)
					matricula="HYFJw39"
					body = {"matricula":matricula}
					r = requests.get('http://craaxcloud.epsevg.upc.edu:19002/api/comprovar-estat-coche', data = body)
					r.status_code
					get_json = r.json()
					if x
						IP = line.split()[2]

					# Aqui iria la consulta de la base de datos ya sea la del cloud o una local que creemos para los estados.
					# Si es true que su estado es disponible, devolvemos esta ip, sino, seguimos mirando los demas archivos.
					# La consulta se haria con la matricula.
					return IP

	#Si el codigo llega aqui, significa que no ha encontrado ninguna IP con estado disponible. Tendriamos que devolver algo para que lo vuelva a intentar en x segundos.
	return "noIP"

def CochesDisponibles():
	CochesLibres = 0
	print("Entra funcion")
	for x in os.listdir('/root/matriculasValidas'):
		# Registramos la direccion del archivo para poder abrirlo
		aux2 = "/root/matriculasValidas/" + str(x)
		with open (aux2) as origin_file:
			#Vamos leyendo linea por linea
			for i,line in enumerate(origin_file):
				if i == 3:
				      	matricula = line.rstrip("\n")
					body = {"matricula":matricula}
					r = requests.get('http://craaxcloud.epsevg.upc.edu:19002/api/comprovar-estat-coche', data = body)
					r.status_code
					get_json = r.json()
					print(get_json)
					if 
						
						CochesLibres = CochesLibres + 1
	return CochesLibres



def SalidasNube():
	for x in os.listdir('/root/Computados'):
		dir_archivo = "/root/Computados/" + str(x)
		#Hacemos el SCP
		p = subprocess.Popen (["scp", dir_archivo, "root@"+IP+":/root/comp"])
		# Esperamos a que termine el envio.
		sts = os.waitpid(p.pid, 0)
	
# Ponemos while 1 pq se ejecuta todo el rato, pararemos cuando arranque el coche, ja que para toda la computacion
while 1:
	# Si hay algun archivo
	for x in os.listdir('/root/toExecute'):
		print(x)
		IP = primeraIPDisponible()
		print(IP)
		while IP == "noIP":
			time.sleep(5)
			IP = primeraIPDisponible()

		dir_programa = "/root/toExecute/" + str(x)
		print (dir_programa)
		#Hacemos el SCP
		p = subprocess.Popen (["scp", dir_programa, "root@"+IP+":/root/comp"])
		# Esperamos a que termine el envio.
		sts = os.waitpid(p.pid, 0)

		# Actualización del estado del coche en la API
		body = {"matricula":matricula, "estado_coche":"2"}
		request = requests.post('http://craaxcloud.epsevg.upc.edu:19002/api/actualizar-estat-coche', data = body)
		request.status_code

		#Ahora que el programa ya se ha mandado al agente en cuestion, lo eliminamos del server.
		os.remove(dir_programa)

	# Pongo un sleep de cinco para no se satura el ordenador
time.sleep(5)
