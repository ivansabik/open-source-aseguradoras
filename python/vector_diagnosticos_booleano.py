# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import time

tiempo_inicio = time.time()

siniestros = pd.read_csv('Salud2012.csv')

# Función para transformar sexo en booleano
siniestros_m = siniestros[siniestros['SEXO']=='M']
siniestros_m['MASCULINO'] = 1
siniestros_f = siniestros[siniestros['SEXO']=='F']
siniestros_f['MASCULINO'] = 0
siniestros = pd.concat([siniestros_m, siniestros_f])
siniestros.drop('SEXO', axis=1, inplace=True)
print siniestros.head()

# Función para diagnóstico con indicador booleano 
def myfunc(group):
    diagnostico = list(group.DIAGNOST1)[0]
    group[diagnostico] = 1
    return group

siniestros = siniestros.groupby('DIAGNOST1').apply(myfunc)
siniestros.fillna(0, inplace=True)

# Escribe archivo CSV transformado
siniestros.to_csv('Salud2012_booleanos.csv')


# Estadísticas generales

print '----------'
print 'Tiempo: ' + str(time.time() - tiempo_inicio) + ' segs.'
