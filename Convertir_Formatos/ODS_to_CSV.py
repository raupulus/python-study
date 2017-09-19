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
##    Importar Librerías    ##
##############################

from pyexcel_ods import get_data


##############################
##         Variables        ##
##############################

lines = get_data("test.ods")

#Extraer cada línea encontrada

#Pasar cada línea al archivo csv

#print(data)

#Ejemplo en JSON
#import json
#print(json.dumps(data))
#{"Sheet 1": [[1, 2, 3], [4, 5, 6]], "Sheet 2": [["row 1", "row 2", "row 3"]]}


x = 0
for line in lines:
	print(x)
	print(line) #Ahora mismo solo dibuja el número de hoja
	x = x + 1