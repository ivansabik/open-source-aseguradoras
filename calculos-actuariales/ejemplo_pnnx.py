# -*- coding: utf-8 -*-

import csv
from calculadora_pnnx import pnnx
import ast
import time

tiempo_inicio = time.time()
f = open('tabla_mortalidad.csv')
reader = csv.reader(f)
tabla_mortalidad = {}
reader.next()
for row in reader:
    tabla_mortalidad[ast.literal_eval(row[0])] = ast.literal_eval(row[1])
f = open('polizas.csv')
reader = csv.reader(f)
reader.next()

calculos_pnnx = {}
for row in reader:
    num_poliza = row[0]
    moneda = row[2]
    tipo_plan = row[3]
    edad = ast.literal_eval(row[4])
    sa = ast.literal_eval(row[5])
    plazo = 5
    calculo_pnnx = pnnx(edad, sa, plazo, moneda, tabla_mortalidad)
    calculos_pnnx[num_poliza] = calculo_pnnx
    print 'Póliza número ' + num_poliza + ', PNNx: ' + str(calculo_pnnx)
print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
