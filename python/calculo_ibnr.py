import pandas as pd
import numpy as np
import copy
import random

# Se carga el archivo con la informacion de emision de polizas y montros de siniestros

csv_sonr = pd.read_csv('archivos-texto/info_sonr.csv', dtype='float')

# Se crea un vector que contiene la info el triangulo SONR, otro con las simulaciones

anios_emision = csv_sonr['anio_emision'].unique()

sonr = pd.DataFrame({'anio_emision': anios_emision, 'prima_emitida': None}, dtype='float')
for anio_desarrollo in range(1,8):
    sonr['s' + str(anio_desarrollo)] = None
sonr = sonr.dropna(subset=['anio_emision'], how='all')
sonr = sonr.set_index('anio_emision')

# Llena el triangulo SONR

def llena_triangulo(csv_sonr):
    anio_emision = csv_sonr['anio_emision']
    if not pd.isnull(csv_sonr['anio_emision']) and not pd.isnull(csv_sonr['prima_emitida']):
        sonr['prima_emitida'].loc[anio_emision] = csv_sonr['prima_emitida']
    if not pd.isnull(csv_sonr['anio_siniestro']) and not pd.isnull(csv_sonr['monto_siniestro']):
        anio_siniestro = csv_sonr['anio_siniestro']
        dif_emision_sin = int(anio_siniestro - anio_emision)
        indice_s = 's' + str(dif_emision_sin)
        sonr[indice_s].loc[anio_emision] = csv_sonr['monto_siniestro']
    return csv_sonr
    
csv_sonr = csv_sonr.apply(llena_triangulo, axis=1)

#Se obtienen los factores de monto siniestro / prima emitida

factores_sonr = copy.deepcopy(sonr)
factores_sonr.reset_index(level=0, inplace=True)

def llena_factores(factores_sonr):
    for i in range(1, 8):
        indice_s = 's' + str(i)
        if not pd.isnull(factores_sonr[indice_s]):
            anio_emision = factores_sonr['anio_emision']
            factores_sonr[indice_s] = sonr[indice_s].loc[anio_emision] / sonr['prima_emitida'].loc[anio_emision]
    return factores_sonr
factores_sonr = factores_sonr.apply(llena_factores, axis=1)
factores_sonr = factores_sonr.set_index('anio_emision')

factores = pd.DataFrame({'limite': ['max', 'min']})
for anio_desarrollo in range(1,8):
    factores['s' + str(anio_desarrollo)] = None
factores = factores.set_index('limite')
    
for i in range(1, 8):
    indice_s = 's' + str(i)
    factores.loc['max'][indice_s] = factores_sonr[indice_s].max() * 1.1 
    factores.loc['min'][indice_s] = factores_sonr[indice_s].min() * 0.9
    
    
# Se simulan los siniestros para las proyecciones (parte inferior del triangulo)

sim_sonr = copy.deepcopy(sonr)
sim_sonr.reset_index(level=0, inplace=True)

def simula_rec(sim_sonr):
    for i in range(1, 8):
        indice_s = 's' + str(i)
        if pd.isnull(sim_sonr[indice_s]):
            anio_emision = sim_sonr['anio_emision']
            max = factores.loc['max'][indice_s]
            min = factores.loc['min'][indice_s]
            prima_emitida = sonr['prima_emitida'].loc[anio_emision]
            sim_sonr[indice_s] = random.uniform(min * prima_emitida, max * prima_emitida)
        else:
            sim_sonr[indice_s] = None
    return sim_sonr
    
sim_sonr = sim_sonr.apply(simula_rec, axis=1)
sim_sonr = sim_sonr.set_index('anio_emision')
sonr.reset_index(level=0, inplace=True)

# Se agrupan los dos triangulos

def combina(sonr):
    for i in range(1, 8):
        indice_s = 's' + str(i)
        if pd.isnull(sonr[indice_s]):
            anio_emision = sonr['anio_emision']
            sonr[indice_s] = sim_sonr.loc[anio_emision][indice_s]
    return sonr

sonr = sonr.apply(combina ,axis=1)
sonr = pd.concat([sonr, pd.DataFrame(sonr.ix[:, 's1':'s7'].sum(axis=1), columns=['rec_brutas'])],axis=1)

print sonr
print sonr['rec_brutas'].sum()
