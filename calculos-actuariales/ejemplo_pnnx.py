# -*- coding: utf-8 -*-
import csv
from calculadora_pnnx import pnnx
import ast
import time

tiempo_inicio = time.time()

# Lee tabla de mortalidad, salta header de csv
archivo_csv = open('tabla_mortalidad.csv')
reader = csv.reader(archivo_csv)
tabla_mortalidad = {}
reader.next()

# Lee pólizas, salta header de csv
for row in reader:
    tabla_mortalidad[ast.literal_eval(row[0])] = ast.literal_eval(row[1])
archivo_csv = open('polizas.csv')
reader = csv.reader(archivo_csv)
reader.next()

# Calcula PNNx por póliza
calculos_pnnx = {}
for row in reader:
    num_poliza = row[0]
    moneda = row[2]
    plazo = int(row[3])
    edad = ast.literal_eval(row[4])
    sa = ast.literal_eval(row[5])
    calculo_pnnx = pnnx(edad, sa, plazo, moneda, tabla_mortalidad)
    calculos_pnnx[num_poliza] = calculo_pnnx
    # print 'Póliza número ' + num_poliza + ', PNNx: ' + str(calculo_pnnx)
print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
