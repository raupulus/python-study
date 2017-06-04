#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============================================================================
# 				Pedir archivo y contar Palabras
# ==============================================================================
nombref = raw_input('Introduzca el nombre del fichero: ')

try:
	manf = open(nombredef)
except:
	print '\nEl archivo %s no se pudo abrir' % nombref
	exit()


