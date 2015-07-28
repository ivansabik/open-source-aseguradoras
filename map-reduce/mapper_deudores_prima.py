#!/usr/bin/env python

import sys

NIVELES = ["1","2","4"]

for linea in sys.stdin:
    linea = linea.strip()
    keys = linea.split('|')
    nivel_1, nivel_2 = keys[0], keys[1]
    if nivel_1 != "140" or nivel_2 not in NIVELES:
        print( "%s\t%d" % (-1, 0) )
    else:
        moneda = keys[4]
        ramo = keys[9]
        primas_por_cobrar = keys[10]
        key = moneda + ramo
        value = float(primas_por_cobrar)
        print( "%s\t%d" % (key, value) )
