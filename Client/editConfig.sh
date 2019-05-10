#! /bin/bash

echo -n "Introdueix el teu nou nom d'usuari: "
read nomUsuari
echo -n "Introdueix la teva nova contrasenya: "
read password
echo -n "Introdueix la teva nova matricula: "
read matricula

{
  echo $nomUsuari
  echo $password
  echo $matricula | tr -d '[:space:]'

} > log/accLog.txt
