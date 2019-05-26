#!/bin/bash

python s.py &
python entraCotxe &
python recursosParking.py &
python subeArchivos &

# Aqui iremos poniendo los diferentes programas que se tengan que ejecutar al arranque.


# Para la ejecucion al arranque de la maquina usaremos la comanda:
# update-rc.d auto-arranque.sh defaults

# Para quitarlo de la ejecucion inicial, usaremos:
# update-rc.d auto.arranque.sh remove
