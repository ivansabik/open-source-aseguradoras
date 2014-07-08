# -*- coding: utf-8 -*-

import csv
from calculadora_pnnx import pnnx

f = open('tabla_mortalidad.csv')
reader = csv.reader(f)
tabla_mortalidad = {}
reader.next()
for row in reader:
    tabla_mortalidad[int(row[0])] = float(row[1])

f = open('polizas.csv')
reader = csv.reader(f)
tabla_mortalidad = {}
reader.next()
for row in reader:
    edad = int(row[0])
    sa = float(row[1])
    plazo = int(row[2])
    moneda = row[3]
    print pnnx(edad, sa, plazo, moneda, tabla_mortalidad)
