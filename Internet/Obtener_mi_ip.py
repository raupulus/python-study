#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

# Este script obtiene la dirección IP del equipo que la ejecuta

##############################
##         LIBRERÍAS        ##
##############################
import urllib2  # Librería para obtener web

def mi_ip():
    # Variable donde guardar la dirección IP
    ip = ''

    # Añadir web html a variable
    web = urllib2.urlopen('http://checkip.dyndns.org').read()

    # Recorrer html descargado en busca de números que conforman la ip
    for line in str(web):
        # Extraer números y puntos separadores
        if line in str(range(10)) + '.':
            ip += line

    print ('La ip es → ' + ip.strip())
    return ip.strip()

print(mi_ip())
