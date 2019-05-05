#!/bin/bash

#Guardem el la nostra matricula en una variable
matricula=$(cat /root/log/accLog.txt | sed -n '3p')

#Executem l'script dels recursos
/usr/local/bin/systemInfo.sh

#Enviem un txt amb els recursos al servidor
scp $matricula.txt root@10.10.6.1:/root

#Creem el directori pels arxius de computació en cas de que no existeixi
mkdir -p /root/comp

while :
do
	#Recorrem tots els fitxers a computar
	for x in `ls /root/comp/`; do

		#Li donem permissos d'execució al fitxer
		chmod +x /root/comp/$x

		#L'executem i guardem el resultat en un txt
		/root/comp/$x > $matricula--$x.txt

		#Enviem el resultat al servidor
		scp $matricula--$x.txt root@10.10.6.1:/root

		#Esborrem el fitxer i el .txt generat per no tornar-lo a computar
		rm /root/comp/$x $matricula--$x.txt
	done
	sleep 5

done
