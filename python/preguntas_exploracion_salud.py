import pandas as pd
import numpy as np

base_salud = pd.read_csv('./archivos-texto/Salud2012.csv')
siniestros = pd.DataFrame()

siniestros['EDAD'] = base_salud['EDAD']
siniestros['DIAGNOST1'] = base_salud['DIAGNOST1']
siniestros['TOTAL_MM'], siniestros['TOTAL_ES_H'] = 0, 0
for i in range(0,10):
    siniestros['TOTAL_MM'] = siniestros['TOTAL_MM'] + base_salud['MMED_D' + str(i)]
for i in range(1, 4):
	siniestros['TOTAL_ES_H'] = siniestros['TOTAL_ES_H'] + base_salud['DIAS_ES_H' + str(i)]

def sexo_bool(registro):
	if registro['SEXO']  == 'M':
		return 1
	else:
		return 0
		
siniestros['SEXO'] = base_salud.apply(sexo_bool, axis=1)

# Maximos, minimos, promedios, estadisticas generales
print siniestros.describe()

# Cual es la enfermedad mas comun en Distrito Federal?
siniestros_df = pd.DataFrame()
siniestros_df = base_salud[base_salud['LUG_RESIDE'] == 9]
siniestros_df['OCURRENCIAS'] = 0
siniestros_df = siniestros_df.groupby('DIAGNOST1').count()['OCURRENCIAS']
enfermedades = pd.read_csv('./archivos-texto/enfermedades.csv')
enfermedades.columns = ['DIAGNOST1', 'descripcion']
siniestros_df = siniestros_df.order()
siniestros_df = pd.DataFrame(siniestros_df)
siniestros_df.reset_index(level=0, inplace=True)

print siniestros_df.merge(enfermedades).tail(5)
