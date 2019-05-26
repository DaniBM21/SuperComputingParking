#!/bin/bash

while 1:
	# Si hay algun archivo
	parking_ID = 0
	max = 0
	for x in os.listdir('/root/toExecute'):
		dir_programa = "/root/toExecute/" + str(x)

		parkings = mysql -u apachitos -p vsp SELECT count(estado_coche) FROM 'plazas', 'coches' WHERE estado_coche = 0 AND plazas.matricula = coches.matricula GROUP BY plazas.parkingID
	
		for num in parkings
			if [parking_ID = 0] then
				max = num
				parking_ID = parking_ID + 1
			else if [num > max]
				max = num
				parking_ID = parking_ID + 1
			
			fi
		done
		 
		#Hacemos el SCP
		dir_parking = "root@10.100.0." + $parking_ID
		$scp dir_programa root@10.100.0.1:/root/toExecute 

	
