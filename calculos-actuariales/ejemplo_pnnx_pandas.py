# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import time

tiempo_inicio = time.time()

i = 0.05

print '---------- Pólizas ----------'
df_polizas = pd.read_csv('polizas.csv')
df_polizas['pnnx'] = None
# Asigna plazo, TODO: que sea de acuerdo a VIN5, VIN10...
df_polizas['plazo'] = 5
print df_polizas.head()
print df_polizas.describe()

print '---------- Tabla Mortalidad ----------'
df_tabla_mortalidad = pd.read_csv('tabla_mortalidad.csv')
df_tabla_mortalidad['px'] = 1-df_tabla_mortalidad['qx']
print df_tabla_mortalidad.head()

print '---------- Tabla Vt ----------'
df_tabla_vt = pd.DataFrame({'Vt': range(0,100), 't': range(0,100)}).astype('float')
def Vt(df_tabla_vt):
    df_tabla_vt['Vt'] = pow(i+1, -df_tabla_vt['t'])
    return df_tabla_vt
df_tabla_vt.apply(Vt, axis=1)
df_tabla_vt['Vt1'] = df_tabla_vt['Vt'].shift(1)
print df_tabla_vt.head()

print '---------- Calculos por poliza ----------'
def multiplica(df_polizas):
    edad_poliza = df_polizas['edad']
    plazo_poliza = df_polizas['plazo']
    indice_x0 = edad_poliza-12
    df_vt = df_tabla_vt.ix[0:plazo_poliza-1].reset_index(drop=True)
    df_mort = df_tabla_mortalidad.ix[indice_x0:indice_x0+plazo_poliza-1].reset_index(drop=True)
    df_pnnx = df_vt.join(df_mort, how='outer')
    df_polizas['numerador'] = df_pnnx['Vt1'] * df_pnnx['px'] * df_pnnx['qx']
    df_polizas['denominador'] = df_pnnx['Vt'] * df_pnnx['px']
    return df_polizas
df_polizas.apply(multiplica, axis=1)
print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
