# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import time
import copy

tiempo_inicio = time.time()

print '---------- Pólizas ----------'
polizas = pd.read_csv('polizas.csv')
print polizas.keys()
print polizas.head()

print '---------- Tabla Mortalidad ----------'
mortalidad = pd.read_csv('tabla_mortalidad.csv')
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
            numerador[t] = vt['vt'].iloc[t] * mortalidad['pxqx'].iloc[(x+t)-13]
            #if(t == 1 or t == 2 or t ==3):
            #    print x, t, vt['vt+1'].iloc[t], mortalidad['px'].iloc[(x+t)-13]
    return numerador
numerador.apply(multiplica_num, axis=1)
print numerador.head()

print '---------- Tabla denominador con factores ----------'
def multiplica_den(denominador):
    x = denominador['x'].astype('int32')
    for t in denominador[1:]:
        t = int(t)
        if(t == 0):
            denominador[t] = mortalidad['pxqx'].iloc[x-13]
        else:
            denominador[t] = vt['vt+1'].iloc[t] * mortalidad['pxqx'].iloc[(x+t)-13]
            #if(t == 1 or t == 2 or t ==3):
            #    print x, t, vt['vt+1'].iloc[t], mortalidad['pxqx'].iloc[(x+t)-13]
    return denominador
denominador.apply(multiplica_den, axis=1)
print denominador.head()

print '---------- PNNx = (SA * num) / denom ----------'
i = 0
for name, group in polizas.groupby(['edad', 'plazo']):
    i = i + 1 
    edad, plazo = name[0], name[1]
    print 'Edad: ' + str(edad), 'Plazo: ' + str(plazo), 'Edad min: ' + str(polizas['edad'].min())
    print numerador[plazo - 1].iloc[edad - polizas['edad'].min()]
    

print 'Total de combinaciones: ' + str(i)

print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
