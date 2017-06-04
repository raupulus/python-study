#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============================================================================
# 				Pedir archivo y contar Palabras
# ==============================================================================
nombref = raw_input('Introduzca el nombre del fichero: ')

try:
	manf = open(nombref)
except:
	print ('\nEl archivo %s no se pudo abrir' % nombref)
	exit()

contadores = dict()

#Este primer bucle lee línea a línea
for linea in manf:
	palabras = linea.split()

	for palabra in palabras:
		if palabra not in contadores:
			contadores[palabra] = 1
		else:
			contadores[palabra] += 1

print(contadores)