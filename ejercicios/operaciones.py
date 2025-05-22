
def sumar(a,b):
    return a + b

def sumar_args(*args):
    suma = args[0]
    for i in args[1:]:
        suma += i
    return suma

def restar(a,b):
    return a - b

def restar(*args):
    resta = args[0]
    for i in args[1:]:
        resta -= i
    return resta

def multiplicar(a,b):
    return a * b

def multiplicar_args(*args):
    multiplicar = args[0]
    for i in args[1:]:
        multiplicar *= i
    return multiplicar

def dividir(a,b):
    return a / b

def dividir_args(*args):
    dividir = args[0]
    for i in args[1:]:
        dividir /= i
    return dividir

def potenciar(a,b):
    resultado = a ** b
    return resultado

def potenciar_args(*args):
    resultado = args[0]
    for i in args[1:]:
        resultado **= i
    return resultado

def raiz_cuadrada(a):
    resultado = a ** 0.5
    return round(resultado)
