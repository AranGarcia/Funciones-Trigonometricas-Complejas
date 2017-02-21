import cmath
import math

import exponencial_compleja as exp_cmplx


def calculosTrigonometricos(z):
    """
    calcuar_func_tr(numero_complejo) -> [sen(z), cos(z), tan(z), 
        csc(z), sec(z), cot(z), senh(z), cos(z), tan(z)]

    Devuelve una lista con los resultados de aplicar funciones
    trigonométricas a un número complejo

    Argumento:
    z: numero complejo

    """
    resultados = []

    resultados.append(cmath.sin(z))
    resultados.append(cmath.cos(z))
    resultados.append(cmath.tan(z))
    resultados.append(cmplxcsc(z))
    resultados.append(cmplxsec(z))
    resultados.append(cmplxcot(z))
    resultados.append(cmath.sinh(z))
    resultados.append(cmath.cosh(z))
    resultados.append(cmath.tanh(z))

    return resultados

#Fin funcion calculosTrigonometricos

def cmplxcsc(z):
    """
    cmplxcsc(z) -> z0

    Calcula el cosecante de un número complejo.

    Argumento:
    z = numero complejo
    """
    return 1 / cmath.sin(z)
#Fin funcion cmplxcsc

def cmplxsec(z):
    """
    cmplxsec(z) -> z0

    Calcula el secante de un número complejo.

    Argumento:
    z = numero complejo
    """
    return 1 / cmath.cos(z)
#Fin función cmplxsec

def cmplxcot(z):
    """
    cmplxcot(z) -> z0

    Calcula el cotangentes de un número complejo.

    Argumento:
    z = numero complejo
    """
    return 1 / cmath.tan(z)
#Fin función cmplxcot