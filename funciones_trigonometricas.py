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

    resultados.append(cmplxsin(z))
    resultados.append(cmplxcos(z))
    resultados.append(cmplxtan(z))
    resultados.append(cmplxcsc(z))
    resultados.append(cmplxsec(z))
    resultados.append(cmplxcot(z))
    resultados.append(cmplxsenh(z))
    resultados.append(cmplxcosh(z))
    resultados.append(cmplxtanh(z))

    return resultados

#Fin funcion calculosTrigonometricos

def cmplxsin(z):
    """
    cmplxsin(z) -> z0

    Calcula el seno de un número complejo.

    Argumento:
    z = numero complejo
    """
    return (exp_cmplx.expiz(z) - exp_cmplx.expiz(z, True) ) / 2j
#Fin función cmplxsin

def cmplxcos(z):
    """
    cmplxcos(z) -> z0

    Calcula el coseno de un número complejo.

    Argumento:
    z = numero complejo
    """
    return (exp_cmplx.expiz(z) + exp_cmplx.expiz(z, True) ) / 2
#Fin funcion cmplxcos

def cmplxtan(z):
    """
    cmplxtan(z) -> zs

    Calcula la tangente de un número complejo.

    Argumento:
    z = numero complejo
    """
    return cmplxsin(z) / cmplxcos(z)
#Fin funcion cmplxtan

def cmplxcsc(z):
    """
    cmplxcsc(z) -> z0

    Calcula el cosecante de un número complejo.

    Argumento:
    z = numero complejo
    """
    return 1 / cmplxsin(z)
#Fin funcion cmplxcsc

def cmplxsec(z):
    """
    cmplxsec(z) -> z0

    Calcula el secante de un número complejo.

    Argumento:
    z = numero complejo
    """
    return 1 / cmplxcos(z)
#Fin función cmplxsec

def cmplxcot(z):
    """
    cmplxcot(z) -> z0

    Calcula el cotangentes de un número complejo.

    Argumento:
    z = numero complejo
    """
    return 1 / cmplxtan(z)
#Fin función cmplxcot

def cmplxsenh(z):
    """
    cmplxsenh(z) -> z0

    Calcula el seno hiperbólico de un número complejo.

    Argumento:
    z = numero complejo
    """
    return (exp_cmplx.expz(z) - exp_cmplx.expz(z, True) ) / 2
#Fin funcion cmplxsenh

def cmplxcosh(z):
    """
    cmplxsenh(z) -> z0

    Calcula el coseno hiperbólico de un número complejo.

    Argumento:
    z = numero complejo
    """
    return (exp_cmplx.expz(z) + exp_cmplx.expz(z, True) ) / 2
#Fin función cmplxcosh

def cmplxtanh(z):
    """
    cmplxtanh(z) -> z0

    Calcula el seno hiperbólico de un número complejo.

    Argumento:
    z = numero complejo
    """
    return cmplxsenh(z) / cmplxcosh(z)
#Fin función cmplxtanh