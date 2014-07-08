# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

i = 0.05

print '---------- Pólizas ----------'
df_polizas = pd.read_csv('polizas.csv')
print df_polizas.head()
print df_polizas.describe()

print '---------- Tabla Mortalidad ----------'
df_tabla_mortalidad = pd.read_csv('tabla_mortalidad.csv')
df_tabla_mortalidad['px'] = 1-df_tabla_mortalidad['qx']
print df_tabla_mortalidad.head()
print df_tabla_mortalidad.describe()

print '---------- Tabla Vt ----------'
df_tabla_vt = pd.DataFrame({'Vt': range(0,100), 't': range(0,100)})
def Vt(df_tabla_vt):
    df_tabla_vt['Vt'] = float(pow(i+1, -df_tabla_vt['t']))
    return df_tabla_vt
df_tabla_vt.apply(Vt, axis=1)
pd.set_printoptions(precision=10)
print df_tabla_vt.head()
print df_tabla_vt.describe()
