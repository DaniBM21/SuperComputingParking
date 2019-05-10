#! /bin/bash

echo -n "Introdueix el teu nom d'usuari: "
read nomUsuari
echo -n "Introdueix la teva contrasenya: "
read password
echo -n "Introdueix la teva matricula: "
read matricula

{
  echo $nomUsuari
  echo $password
  echo $matricula | tr -d '[:space:]'

} > log/accLog.txt

chmod -x $0
