def pnnx(edad, sa, plazo, tabla_mortalidad):
    x, n, i = edad,plazo,0.05
    suma_numerador, suma_denominador = 0.0, 0.0
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
