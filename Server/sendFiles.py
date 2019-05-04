#!/usr/bin/python
import time, os, subprocess, re, shutil

def primeraIPDisponible():

	for x in os.walk("/root/Matriculas"):
		# Registramos la direccion del archivo para poder abrirlo
		aux2 = "/root/Matriculas/" + str(x)
		with open (aux2) as origin_file:
			#Vamos leyendo linea por linea
			for line in origin_file:
				# Buscamos si hay "IP" en la linea
				if 'IP' in line:
					IP = line.split()[2]
					# Aqui iria la consulta de la base de datos ya sea la del cloud o una local que creemos para los estados.
					# Si es true que su estado es disponible, devolvemos esta ip, sino, seguimos mirando los demas archivos.	
					return IP

	#Si el codigo llega aquí, significa que no ha encontrado ninguna IP con estado disponible. Tendriamos que devolver algo para que lo vuelva a intentar en x segundos.
	return "noIP"				

# Ponemos while 1 pq se ejecuta todo el rato, pararemos cuando arranque el coche, ja que para toda la computacion
while 1:	
	# Si hay algun archivo
	for x in os.walk("/root/Programas"):
		IP = primeraIPDisponible()				

		while IP == "noIP":
			time.sleep(5)
			IP = primeraIPDisponible()

		dir_programa = "/root/Programas/" + str(x)
		#Hacemos el SCP		
		p = subprocess.Popen (["scp", "dir_programa", "root@"+IP+":/root/Ejecutar"])
		# Esperamos a que termine
		sts = os.waitpid(p.pid, 0).

		#Ahora que el programa ya se ha mandado al agente en cuestion, lo movemos a una subcarpeta de ejecutablesMandados (o podriamos simplemente borrarlo).
		shutil.move(dir_programa, "/root/programasMandados/"+str(x))

	# Pongo un sleep de cinco para no se satura el ordenador
	time.sleep(5)
