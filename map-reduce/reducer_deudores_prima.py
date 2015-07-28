#!/usr/bin/env python

import sys

moneda_ramo_eval = None
monto_eval = 0

for linea in sys.stdin:
    linea = linea.strip()
    moneda_ramo, monto = linea.split('\t')
    monto = float(monto)
    if moneda_ramo_eval == moneda_ramo:
        monto_eval += monto
    else:
        if moneda_ramo_eval:
            print '%s\t%s' % (moneda_ramo_eval, monto_eval)
        monto_eval = monto
        moneda_ramo_eval = moneda_ramo
if moneda_ramo_eval == moneda_ramo:
    print '%s\t%s' % (moneda_ramo_eval, monto_eval)
