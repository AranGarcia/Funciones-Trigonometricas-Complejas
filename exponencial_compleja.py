import math

def expiz(z, exponenteNegativo = False):
    """
    expiz(complejo, indice_es_negativo = False) -> e ^ iz

    Función auxiliar para calcular un exponencial complejo de tipo e ^ iz.
    Si se agrega un segundo argumento, se calcula el exponencial de la forma
    e ^ -iz.

    Argumentos:
    z = número complejo
    exponenteNegativo = Indica si el exponente es negativo
    """
    if exponenteNegativo == False:
        return complex(math.exp( -z.imag) * math.cos( math.radians(z.real)) ,
            math.exp(-z.imag ) * math.sin( math.radians( z.real ) ))
    
    return complex(math.exp( z.imag) * math.cos( -math.radians(z.real)) ,
        math.exp( z.imag ) * math.sin( -math.radians( z.real ) ))
#Fin funcion calcular_eiz

def expz(z, exponenteNegativo = False):
    """
    expz(complejo, indice_es_negativo = False) -> e ^ z

    Función auxilar para calcular un exponencial cmplejo de tipo e ^ z.
    Si se agrega un segundo argumento, se calcula el exponencial de la forma e ^ -iz.

    Argumentos:
    z = numero complejo
    exponenteNegativo = Indica si el exponente es negativo
    """

    if exponenteNegativo == False:
        return complex(math.exp( z.real) * math.cos( math.radians(z.imag)) ,
            math.exp(z.real ) * math.sin( math.radians( z.imag ) ))
    
    return complex(math.exp( -z.real) * math.cos( -math.radians(z.imag)) ,
        math.exp( -z.real) * math.sin( -math.radians( z.imag ) ) )