# -*- coding: utf-8 -*-

def pnnx(edad, sa, plazo, moneda, tabla_mortalidad):
    x = edad
    n = plazo
    if(moneda.lower() == 'mxp'):
        i = 0.05
    elif(moneda.lower() == 'udi'):
        i = 0.025
    elif(moneda.lower() == 'usd'):
        i = 0.03
    else:
        raise NameError('Moneda desconocida!: ' + moneda)
    suma_numerador = 0.0
    suma_denominador = 0.0
    for t in range(0, n):
        vt_mas_1 = pow(1 + i, -(t + 1))
        qx_mas_t = tabla_mortalidad[x + t]
        if (t == 0):
            tpx = 1
        else:
            tpx = 1 - qx_mas_t
        suma_numerador += vt_mas_1 * tpx * qx_mas_t
        vt = pow(1 + i, -t)
        suma_denominador += vt * tpx
    pnnx = (sa * suma_numerador) / suma_denominador
    return pnnx
