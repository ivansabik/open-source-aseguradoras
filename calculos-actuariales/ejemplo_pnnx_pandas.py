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
print df_polizas.describe()

print '---------- Tabla Mortalidad ----------'
df_tabla_mortalidad = pd.read_csv('tabla_mortalidad.csv')
df_tabla_mortalidad['px'] = 1-df_tabla_mortalidad['qx']
df_tabla_mortalidad['pxqx'] = df_tabla_mortalidad['px']-df_tabla_mortalidad['qx']
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
df_tabla_num = pd.DataFrame({'x': sorted(df_polizas['edad'].unique())})
for t in range(0, df_polizas['plazo'].max()):
    df_tabla_num[t] = t
    df_tabla_num[t] = df_tabla_num[t].astype('float')
print df_tabla_num.head()

print '---------- Tabla denominador ----------'
df_tabla_den = copy.deepcopy(df_tabla_num)
print df_tabla_den.head()

print '---------- Tabla numerador con calculos ----------'
def multiplica(df_tabla_num):
    x = df_tabla_num[0].astype('int32')
    for col in df_tabla_num[1:]:
        if(col == 0):
            df_tabla_num[col] = 2000
        else:
            df_tabla_num[col] = df_tabla_vt['Vt1'][col] * df_tabla_mortalidad['pxqx'].shift(-(12-x))[x+col]
            print df_tabla_num[col]
    return df_tabla_num
df_tabla_num.apply(multiplica, axis=1)
print df_tabla_num[0].head()

'''
print '---------- Llenado de x/t ----------'
def multiplica(df_tabla_xt):
    x = df_tabla_xt['x']
    indice_x0 = x - 12

    Vt = df_tabla_vt['Vt'].ix[0:n-1].reset_index(drop=True)
    Vt1 = df_tabla_vt['Vt1'].ix[0:n-1].reset_index(drop=True)
    tPx = df_tabla_mortalidad['px'].ix[indice_x0:indice_x0+n-1].reset_index(drop=True)
    qxt =df_tabla_mortalidad['qx'].ix[indice_x0:indice_x0+n-1].reset_index(drop=True)

    df_tabla_xt['Vt1xtPxxQxt'] = Vt1 * tPx * qxt
    df_tabla_xt['VttPx'] = Vt * tPx

    
    return df_tabla_xt
df_tabla_xt.apply(multiplica, axis=1)

print df_tabla_xt.head()
'''

print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
