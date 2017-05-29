#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

##############################
##         Variables        ##
##############################

nombre = raw_input('Introduzca fichero:')
manejador = open(nombre, 'r')
texto = manejador.read()
palabras = texto.split()
contadores = dict()

##############################
##         PROGRAMA         ##
##############################

for palabra in palabras:
    contadores[palabra] = contadores.get(palabra, 0) + 1

mayorcantidad = None
mayorpalabra = None
for palabra,contador in contadores.items():
    if mayorcantidad is None or contador > mayorcantidad:
        mayorpalabra = palabra
        mayorcantidad = contador

#Estaria bien comparar con la segunda, si coincide la misma cantidad de veces
#comparar con la tercera y asi sucesivamente hasta que no hayan palabras que
#coincidan el mismo número de veces

print ''
print 'La mayor palabra es:'
print mayorpalabra
print
print 'La cantidad de veces repetida es:'
print mayorcantidad
