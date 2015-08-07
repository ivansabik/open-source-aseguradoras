import pandas as pd
import numpy as np
import copy

# Construye DataFrames para  Polizas y tablas de mortalidad
polizas = pd.read_csv('archivos-texto/polizas.csv')
polizas = polizas.set_index('num_poliza')

mortalidad = pd.read_csv('archivos-texto/tabla_mortalidad.csv')
mortalidad = mortalidad.set_index('edad')
mortalidad['px'] = 1 - mortalidad['qx']
mortalidad['pxqx'] = mortalidad['px'] * mortalidad['qx']

# Construye tabla Vt para todas las combinaciones de plazos y edades en el conjunto de datos
i = 0.05
vt = pd.DataFrame({'vt': range(0, polizas['plazo'].max()+1), 't': range(0,polizas['plazo'].max()+1)}, dtype='float')
def Vt(vt):
    vt['vt'] = pow(i+1, -vt['t'])
    return vt
vt.apply(Vt, axis=1)
vt['vt+1'] = vt['vt'].shift(-1)

# Tabla numerador
numerador = pd.DataFrame({'x': sorted(polizas['edad'].unique())}, dtype='float')
for t in range(0, polizas['plazo'].max()):
    numerador[t] = t
    numerador[t] = numerador[t].astype('float')

# Tabla denominador
denominador = copy.deepcopy(numerador)

# Funcion de tansformacion para numerador
def multiplica_num(numerador):
    x = numerador['x'].astype('int32')
    for t in numerador[1:]:
        t = int(t)
        if(t == 0):
            numerador[t] = vt['vt'].iloc[t] 
        else:
            numerador[t] = vt['vt'].iloc[t] * mortalidad['pxqx'].iloc[x + t]
    return numerador
numerador = numerador.apply(multiplica_num, axis=1)

# Funcion de transfomacion para denominador
def multiplica_den(denominador):
    x = denominador['x'].astype('int32')
    for t in denominador[1:]:
        t = int(t)
        if(t == 0):
            denominador[t] = mortalidad['pxqx'].iloc[x]
        else:
            denominador[t] = vt['vt+1'].iloc[t] * mortalidad['pxqx'].iloc[x + t]
    return denominador
denominador = denominador.apply(multiplica_den, axis=1)

# Calcula columna PNNx = (SA * num) / denom
polizas['pnnx'] = None
def pnnx(sa, edad, plazo):
    return sa * numerador[plazo - 1].iloc[0:edad].sum() / denominador[plazo - 1].iloc[0:edad].sum()
polizas_agrupadas = polizas.groupby(['edad', 'plazo'])
tuplas_polizas = dict(list(polizas_agrupadas)).keys()
for tupla in tuplas_polizas:
    edad, plazo = tupla[0], tupla[1]
    polizas['pnnx'] = polizas_agrupadas['suma_asegurada'].apply(pnnx, edad, plazo)

print polizas.head()
