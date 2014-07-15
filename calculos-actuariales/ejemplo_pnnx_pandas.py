# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import time
import copy
from itertools import chain

tiempo_inicio = time.time()

print '---------- Pólizas ----------'
polizas = pd.read_csv('polizas.csv')
polizas = polizas.set_index('num_poliza')
polizas['pnnx'] = None
print polizas.keys()
print polizas.head()

print '---------- Tabla Mortalidad ----------'
mortalidad = pd.read_csv('tabla_mortalidad.csv')
mortalidad = mortalidad.set_index('edad')
mortalidad['px'] = 1-mortalidad['qx']
mortalidad['pxqx'] = mortalidad['px']*mortalidad['qx']
print mortalidad.head()

print '---------- Tabla Vt ----------'
i = 0.05
vt = pd.DataFrame({'vt': range(0,polizas['plazo'].max()+1), 't': range(0,polizas['plazo'].max()+1)}, dtype='float')
def Vt(vt):
    vt['vt'] = pow(i+1, -vt['t'])
    return vt
vt.apply(Vt, axis=1)
vt['vt+1'] = vt['vt'].shift(-1)
print vt.head()

print '---------- Edades ----------'
print sorted(polizas['edad'].unique())
print polizas['edad'].max()
print polizas['edad'].min()

print '---------- Plazos ----------'
print sorted(polizas['edad'].unique())
print polizas['plazo'].max()
print polizas['plazo'].min()

print '---------- Tabla numerador ----------'
numerador = pd.DataFrame({'x': sorted(polizas['edad'].unique())}, dtype='float')
for t in range(0, polizas['plazo'].max()):
    numerador[t] = t
    numerador[t] = numerador[t].astype('float')
print numerador.head()

print '---------- Tabla denominador ----------'
denominador = copy.deepcopy(numerador)
print numerador.head()

print '---------- Tabla numerador con factores ----------'
def multiplica_num(numerador):
    x = numerador['x'].astype('int32')
    for t in numerador[1:]:
        t = int(t)
        if(t == 0):
            numerador[t] = vt['vt'].iloc[t] 
        else:
            numerador[t] = vt['vt'].iloc[t] * mortalidad['pxqx'].iloc[x+t]
    return numerador
numerador.apply(multiplica_num, axis=1)
print numerador.head()

print '---------- Tabla denominador con factores ----------'
def multiplica_den(denominador):
    x = denominador['x'].astype('int32')
    for t in denominador[1:]:
        t = int(t)
        if(t == 0):
            denominador[t] = mortalidad['pxqx'].iloc[x]
        else:
            denominador[t] = vt['vt+1'].iloc[t] * mortalidad['pxqx'].iloc[x+t]
    return denominador
denominador.apply(multiplica_den, axis=1)
print denominador.head()

print '---------- PNNx = (SA * num) / denom ----------'
def pnnx(sa, edad, plazo):
    return sa * numerador[plazo - 1].iloc[0:edad].sum() / denominador[plazo - 1].iloc[0:edad].sum()
polizas_agrupadas = polizas.groupby(['edad', 'plazo'])
for keys_grupo in dict(list(polizas_agrupadas)).keys():
    edad, plazo = keys_grupo[0], keys_grupo[1]
    polizas['pnnx'] = polizas_agrupadas['suma_asegurada'].apply(pnnx, edad, plazo)

print polizas.head()
print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
