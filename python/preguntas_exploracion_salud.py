# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

siniestros_original = pd.read_csv('./archivos-texto/Salud2012.csv')
siniestros = pd.DataFrame()

siniestros['EDAD'] = siniestros_original['EDAD']
siniestros['SEXO'] = siniestros_original['SEXO']
siniestros['DIAGNOST1'] = siniestros_original['DIAGNOST1']
for i in range(0,9):
    siniestros['MMED_D' + str(i)] = siniestros_original['MMED_D' + str(i)]
siniestros['DIAS_ES_H1'] = siniestros_original['DIAS_ES_H1']
siniestros['DIAS_ES_H2'] = siniestros_original['DIAS_ES_H2']
siniestros['DIAS_ES_H3'] = siniestros_original['DIAS_ES_H3']
siniestros['LUG_RESIDE'] = siniestros_original['LUG_RESIDE']
siniestros['TOTAL_MM'] = 0
for i in range(0,9):
    siniestros['TOTAL_MM'] = siniestros['TOTAL_MM'] + siniestros['MMED_D' + str(i)]
siniestros['TOTAL_ES_H'] = siniestros['DIAS_ES_H1']
siniestros['TOTAL_ES_H'] = siniestros['TOTAL_ES_H'] + siniestros['DIAS_ES_H2']
siniestros['TOTAL_ES_H'] = siniestros['TOTAL_ES_H'] +siniestros['DIAS_ES_H3']


# Máximos, mínimos, promedios, estadísticas generales
print siniestros.describe()

# ¿Qué porcentaje de reclamos son para hombres y cuál para mujeres?
siniestros_m = siniestros[siniestros['SEXO']=='M']
siniestros_f = siniestros[siniestros['SEXO']=='F']
print len(siniestros_m) / float(len(siniestros)) * 100
print len(siniestros_f) / float(len(siniestros)) * 100

# ¿Cuál es la enfermedad más común en Distrito Federal?
siniestros_distrito = siniestros[siniestros['LUG_RESIDE'] == 9]
siniestros_distrito['OCURRENCIAS'] = None
siniestros_distrito = siniestros_distrito.groupby('DIAGNOST1').count()['OCURRENCIAS']
enfermedades = pd.read_csv('./archivos-texto/enfermedades.csv')
enfermedades.columns = ['DIAGNOST1', 'descripcion']
siniestros_distrito = siniestros_distrito.order()
siniestros_distrito = pd.DataFrame(siniestros_distrito)
siniestros_distrito.reset_index(level=0, inplace=True)
print siniestros_distrito.merge(enfermedades).tail(30)
