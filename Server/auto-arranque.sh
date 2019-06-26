#!/bin/bash

python3 server.py &
python3 entraCotxe.py &
python3 recursosParking.py &
python3 subeArchivos.py &
python3 surtCotxe.py
# Aqui iremos poniendo los diferentes programas que se tengan que ejecutar al arranque.


# Para la ejecucion al arranque de la maquina usaremos la comanda:
# update-rc.d auto-arranque.sh defaults

# Para quitarlo de la ejecucion inicial, usaremos:
# update-rc.d auto.arranque.sh remove
