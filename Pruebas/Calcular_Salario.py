#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
# Calcula el salario pidiendo número de horas y tarifa
# ==============================================================================

horas = raw_input('Introduce el número de horas: ')
tarifa = raw_input('Introduce la tarifa por hora: ')
salario = int(horas) * int(tarifa)

print(salario)