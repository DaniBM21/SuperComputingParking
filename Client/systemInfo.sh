#! /bin/bash

matricula=$(cat /root/log/accLog.txt  | sed -n '3p')
#Comprovamos si existe el archivo info.txt, lo borramos para actualizar-lo.
[ -e /root/log/$matricula.txt ] && rm /root/log/$matricula.txt

{
    echo "##########Información Usuario##########"
    cat log/accLog.txt

    #Información general del sistema.
    echo -e "\n\n\n##########Información General##########"
    echo "Sistema Operativo: $(hostnamectl | grep "Operating System:" | awk '{print substr($0,index($0,$3))}')"
    echo "Kernel: $(hostnamectl | grep "Kernel:" | awk '{print substr($0,index($0,$2))}')"
    echo "Dirección MAC: $(ip ad | grep -m1 "ether" | awk '{print $2}')"
    echo "Dirección IP: $(hostname -I)"


    #Información de la CPU del sistema.
    echo -e "\n\n############Información CPU############"
    echo "Arquitectura: $(lscpu | grep "Arquitectura:" | awk '{print $2}')"
    echo "Modo operación: $(lscpu | grep "operación" | cut -d: -f2)"
    echo "CPU(s): $(lscpu | grep -m1 "CPU(s):" | awk '{print $2}')"
    echo "Frecuencia: $(lscpu | grep "CPU MHz:" | awk '{print $3}')"
#   echo "Frecuencia máxima: $(lscpu | grep "CPU max" | awk '{print $4}' | cut -d, -f1)MHz"
#   echo "Frecuencia mínima: $(lscpu | grep "CPU min" | awk '{print $4}' | cut -d, -f1)MHz"
    echo "Load Average (1 min): $(uptime | awk '{print $9}' | cut -d, -f1,2)"
    echo "Load Average (5 min): $(uptime | awk '{print $10}' | cut -d, -f1,2)"
    echo "Load Average (15 min): $(uptime | awk '{print $11}' | cut -d, -f1,2)"


    #Información de la memoria principal del sistema.
    echo -e "\n\n############Información RAM############"
    echo "Total: $(free -m | grep "Mem" | awk '{print $2}')"
    echo "En uso: $(free -m | grep "Mem" | awk '{print $3}')"
    echo "Disponible: $(free -m | grep "Mem" | awk '{print $7}')"


    #Información de los discos duros del sistema.
    echo -e "\n\n############Información HDD############"
    while read -r line; do
    	if echo $line | awk '{print $1}' | grep -q "/dev"; then
    		echo "Dispositivo: $(echo $line | grep "/dev/" | awk '{print $1}')"
    		echo "Espacio total: $(echo $line | grep "/dev/" | awk '{print $2}')"
    		echo "Espacio usado: $(echo $line | grep "/dev/" | awk '{print $3}') ($(echo $line | grep "/dev/" | awk '{print $5}'))"
    		echo -e "Espacio disponible: $(echo $line | grep "/dev/" | awk '{print $4}')\n"
    	fi
    done < <(df -H)

} > /root/log/$matricula.txt
