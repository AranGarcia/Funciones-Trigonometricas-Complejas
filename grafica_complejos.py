import math
import matplotlib.pyplot as plt
import numpy

def graficar_complejos(z, lista_complejos = None, ):
    """
    graficar_complejos(lista_complejos)
    Abre una nueva venta en la que se muestra un plano complejo
    y todos los números complejos en la lista que se pasó como argumento

    Argumentos:
    z: El numero complejo al que se le aplican funciones trigonométricas.
        Ayuda a agregar el título de la ventana.
    lista_complejos: lista con todos los numeros complejos a graficar
    """
    if lista_complejos == None:
        return

    #Prepara la ventana donde se va graficar
    fig = plt.gcf()
    fig.canvas.set_window_title("Funciones Trigonométricas de " + str(z))
    plt.ylabel('Imaginarios')
    plt.xlabel("Reales")
    plt.axis('equal')
    plt.grid()

    #Dibuja lineas desde el origen al número complejo
    etiquetas = ("e^z", "sen(z)", "cos(z)", "tan(z)", "csc(z)", "sec(z)",
        "cot(z)", "senh(z)", "cosh(z)", "tanh(z)")

    tipos_lineas = ("bo", "go", "ro", "co", "mo", "yo", "ko", "bD", "rD", "gD")

    for i in range(len(lista_complejos)):
        plt.plot([numpy.real(lista_complejos[i])], [numpy.imag(lista_complejos[i])],
            tipos_lineas[i], label = etiquetas[i])

    #Obtiene las leyendas para cada punto
    ax = plt.gca()
    handles, etiquetas = ax.get_legend_handles_labels()
    ax.legend(handles, etiquetas)

    plt.show()