# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import time
import copy

tiempo_inicio = time.time()

i = 0.05

print '---------- Pólizas ----------'
df_polizas = pd.read_csv('polizas.csv')
df_polizas['pnnx'] = None
print df_polizas.head()

print '---------- Tabla Mortalidad ----------'
df_tabla_mortalidad = pd.read_csv('tabla_mortalidad.csv')
df_tabla_mortalidad['px'] = 1-df_tabla_mortalidad['qx']
df_tabla_mortalidad['pxqx'] = df_tabla_mortalidad['px']*df_tabla_mortalidad['qx']
print df_tabla_mortalidad.head()

print '---------- Tabla Vt ----------'
df_tabla_vt = pd.DataFrame({'Vt': range(0,100), 't': range(0,100)}, dtype='float')
def Vt(df_tabla_vt):
    df_tabla_vt['Vt'] = pow(i+1, -df_tabla_vt['t'])
    return df_tabla_vt
df_tabla_vt.apply(Vt, axis=1)
df_tabla_vt['Vt1'] = df_tabla_vt['Vt'].shift(-1)
print df_tabla_vt.head()

print '---------- Valores únicos de edad ----------'
print sorted(df_polizas['edad'].unique())

print '---------- Plazo máximo ----------'
print df_polizas['plazo'].max()

print '---------- Tabla numerador ----------'
df_tabla_num = pd.DataFrame({'x': sorted(df_polizas['edad'].unique())}, dtype='float')
for t in range(0, df_polizas['plazo'].max()):
    df_tabla_num[t] = t
    df_tabla_num[t] = df_tabla_num[t].astype('float')
print df_tabla_num.head()

print '---------- Tabla denominador ----------'
df_tabla_den = copy.deepcopy(df_tabla_num)
print df_tabla_den.head()

print '---------- Tabla numerador con calculos ----------'
def multiplica(df_tabla_num):
    x = df_tabla_num['x'].astype('int32')
    for t in df_tabla_num[1:]:
        t = int(t)
        if(t == 0):
            df_tabla_num[t] = df_tabla_mortalidad['pxqx'].iloc[x-13]
        else:
            df_tabla_num[t] = df_tabla_vt['Vt1'].iloc[t] * df_tabla_mortalidad['pxqx'].iloc[(x+t)-13]
            if(t == 1 or t == 2 or t ==3):
                print x, t, df_tabla_vt['Vt1'].iloc[t], df_tabla_mortalidad['pxqx'].iloc[(x+t)-13]
    return df_tabla_num
df_tabla_num.apply(multiplica, axis=1)
print df_tabla_num

print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
