#!/bin/bash

while true; do
	for dir_programa in /var/www/html/dashboard/uploads/*.py; do
		parkingID=$(mysql -u apachito -pvsp -sNe "SELECT parkingID,count(estado_coche) as c FROM plazas, coches WHERE estado_coche = 1 AND plazas.matricula = coches.matricula GROUP BY plazas.parkingID ORDER BY c DESC LIMIT 1" vilanovasp | awk '{print $1}')
		#El primer parking tiene IP 10.100.0.10
		parkingID=$(($parkingID + 8))
		#Hacemos el SCP
		dir_parking="root@10.100.0."${parkingID}
		scp $dir_programa $dir_parking:/root/toExecute
		#rm dir_programa
		sleep 2
	done
	sleep 5
done
