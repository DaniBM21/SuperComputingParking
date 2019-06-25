import os, time, requests, json
#_ip='http://craaxcloud.epsevg.upc.edu:19002/api/actualitzar-recursos-parking'
_ip='http://10.100.0.1:3002/api/actualitzar-recursos-parking'


##Funcion que recorre todos los archivos en matriculasValidas y suma los parametros de interes.
##Seguidamente, hace un update en una tabla de la BD mediante la API.
def sumResources(_parkingID):
	_clockRate = 0
	_cpuCores = 0
	_ram = 0
	_ram_used = 0
	_hddSpace = 0
	_hddSpace_used = 0
	for x in os.listdir('matriculasValidas'):
			file = 'matriculasValidas/' + str(x)
			with open(file) as current_file:
				for line in current_file:
					if 'CPU(s)' in line:
						_cpuCores += int(line.split()[1])

					elif 'Frecuencia' in line:
						_clockRate += float(line.split()[1])

					elif 'Total:' in line:
						_ram += int(line.split()[1])

					elif 'En uso:' in line:
						_ram_used += int(line.split()[2])

					elif 'Espacio total:' in line:
						_hddSpace += float((line.split()[2]).replace(',','.'))

					elif 'Espacio usado:' in line:
						_hddSpace_used += float((line.split()[2]).replace(',','.'))



	print(_parkingID,_clockRate,_cpuCores,_ram,_ram_used,_hddSpace,_hddSpace_used)
	tableUpdate(_parkingID,_clockRate,_cpuCores,_ram,_ram_used,_hddSpace,_hddSpace_used)

##Hace un update en una tabla con una llamada a la API.
def tableUpdate(_parkingID,_clockRate,_cpuCores,_ram,_ram_used,_hddSpace,_hddSpace_used):
	body = {'parkingID':_parkingID,'clockRate':_clockRate,'cpuCores':_cpuCores,'ramAvailable':_ram,'ramUsed':_ram_used,'hddSpaceAvailable':_hddSpace,'hddSpaceUsed':_hddSpace_used}
	request = requests.post(_ip,data = body)
	print(request.status_code)

def main():
	while 1:
		sumResources(2)
		time.sleep(10)


main()
