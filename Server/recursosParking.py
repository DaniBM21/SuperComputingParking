import os, time, requests, json

##Funcion que recorre todos los archivos en matriculasValidas y suma los parametros de interes.
##Seguidamente, hace un update en una tabla de la BD mediante la API.
def sumResources():
	_clockRate = 0
	_cpuCores = 0
	_ram = 0
	_hddSpace = 0
	for x in os.listdir('/root/matriculasValidas'):
			file = '/root/matriculasValidas' + str(x)
			with open(file) as current_file:
				for line in current_file:
					if 'CPU(s)' in line:
						_cpuCores += int(line.split()[1])

					elif 'Frecuencia' in line:
						_clockRate += float(line.split()[1])

					elif 'Total:' in line:
						_ram += int(line.split()[1])

					elif 'Espacio disponible:' in line:
						_hddSpace += float((line.split[2]).replace(',','.'))


		tableUpdate(_clockRate,_cpuCores,_ram, _hddSpace)


##Hace un update en una tabla con una llamada a la API.
def tableUpdate(_clockRate,_cpuCores,_ram,_totalHDD_space):
	body = {"clockRate":"_clockRate","cpuCores":"_cpuCores","ram":"_ram","hddSpace":"_hddSpace"}
	request = requests.post('http://craaxcloud.epsevg.upc.edu:19002/api/llamadaApi',data=body)

def main():
	while 1:
		sumResources()
		time.sleep(20)


main()
