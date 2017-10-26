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
import datetime


class info():

    # Obtener nombre para el usuario actual
    def getUser(self):
        user = os.getlogin()
        return user

    # Obtener nombre del Equipo
    def getSysName(self):
        sysName = os.uname()[1]
        return sysName

    # Obtener tipo del Sistema Operativo
    def getSysType(self):
        sysType = os.uname()[0]
        return sysType

    # Obtener Versión del Kernel
    def getSysKernel(self):
        sysKernel = os.uname()[2]
        return sysKernel

    # Obtener Fecha y Hora actual en el sistema
    def getFullDate(self):
        fecha = datetime.datetime.today()
        return fecha
