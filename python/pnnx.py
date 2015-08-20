import csv
from calculadora_pnnx import pnnx
import ast
import time

# Lee tabla de mortalidad, salta header de csv
archivo_csv = open('archivos-texto/tabla_mortalidad.csv')
reader = csv.reader(archivo_csv)
tabla_mortalidad = {}
reader.next()

# Lee polizas, salta header de csv
for edad in reader:
    tabla_mortalidad[ast.literal_eval(edad[0])] = ast.literal_eval(edad[1])
archivo_csv = open('archivos-texto/polizas.csv')
reader = csv.reader(archivo_csv)
reader.next()

# Calcula PNNx por poliza
calculos_pnnx = {}
for registro_poliza in reader:
    num_poliza = registro_poliza[0]
    plazo = int(registro_poliza[1])
    edad = ast.literal_eval(registro_poliza[2])
    sa = ast.literal_eval(registro_poliza[3])
    calculo_pnnx = pnnx(edad, sa, plazo, tabla_mortalidad)
    calculos_pnnx[num_poliza] = calculo_pnnx
    print 'Poliza num ' + num_poliza + ', PNNx: ' + str(calculo_pnnx)
