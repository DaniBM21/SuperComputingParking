#!/usr/bin/python
import time, os, subprocess, re, requests, json

def subeArchivo():
    for x in os.listdir('/root/executed/'):
        x = str(x)
        matricula=x.split("--")[0]
        archivo=x.split("--")[1]
        body = {"matricula":matricula, "estado_coche":"1"}
        request = requests.post('https://10.100.0.1:3002/api/actualitzar-estat-cotxe', data = body, verify=False)
        request.status_code
        os.rename('/root/executed/'+x,'/root/executed/'+archivo)
        archivo = '/root/executed/' + archivo
        p = subprocess.Popen (["scp", "-i", "id_rsa", archivo, "ptin@10.100.0.1:/var/www/html/dashboard/downloads"])
        # Esperamos a que termine el envio.
        sts = os.waitpid(p.pid, 0)
        os.remove(archivo)

def main():
    while 1:
        subeArchivo()
        time.sleep(10)

main()
