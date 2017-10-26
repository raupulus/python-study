#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

# Script que contiene una clase, la cual al instanciarla creará
# un objeto con todos los datos del sistema que estamos usando
# de forma que será accesible desde fuera
# Sistema operativo → Linux

##############################
##         LIBRERÍAS        ##
##############################
import os


class info():

    # Obtener nombre para el usuario actual
    def getUser(self):
        user = os.getlogin()
        return user
