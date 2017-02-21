#!/usr/bin/python3

import cmath
import funciones_trigonometricas as ft
import grafica_complejos as graf

print("\nCalculador de funciones trigonométricas de un número complejo.\n")

entradaInvalida = True
while entradaInvalida:
    try:
        z = complex ( input("Introduce un número complejo z = ") )
        entradaInvalida = False
    except ValueError:
        print("\nERROR: Número complejo inválido.\nEntrada debe ser de la forma a+bj (sin espacios)\n")
    except EOFError:
        print("\n")
        exit("Terminó ejecución.")


resultados = ft.calculosTrigonometricos(z)
resultados.insert(0, cmath.exp(z))

funciones = ("exp(z) =", "sen(z) =", "cos(z) =", "tan(z) =", "csc(z) =",
    "sec(z) =", "cot(z) =", "senh(z) =", "cosh(z) =", "tanh(z) =")

for i in range( len(resultados) ):
    print( funciones[i], resultados[i] )

graf.graficar_complejos(z, resultados)