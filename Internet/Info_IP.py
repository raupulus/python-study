#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

# Función para obtener información sobre una IP pasada como parámetro
# En caso de no recibir una IP tomará nuestra IP pública
# Se depende del paquete "geoiplookup" en el sistema operativo

##############################
##         LIBRERÍAS        ##
##############################
import commands

def getPais(IP):

    # Extraer cadena con el pais
    pais = commands.getoutput("geoiplookup " + str(IP))

    # Limpiar País
    pais = pais.split('\n')[0].split(': ')[1]

