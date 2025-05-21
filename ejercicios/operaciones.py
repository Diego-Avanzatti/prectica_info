
def suma(a,b):
    return a + b

def suma_args(*args):
    suma = args[0]
    for i in args[1:]:
        suma += i
    return suma

def resta(a,b):
    return a - b

def resta(*args):
    resta = args[0]
    for i in args[1:]:
        resta -= i
    return resta

def multiplicacion(a,b):
    return a * b

def multiplicacion_args(*args):
    multiplicar = args[0]
    for i in args[1:]:
        multiplicar *= i
    return multiplicar

def division(a,b):
    return a / b

def division_args(*args):
    dividir = args[0]
    for i in args[1:]:
        dividir /= i
    return dividir

def potencia(numero,potencia = 2):
    resultado = numero ** potencia
    return resultado

def potencia_args(*args):
    potencia = args[0]
    for i in args[1:]:
        potencia **= i
    return potencia

def raiz_cuadrada(numero, decimal = 2):
    resultado = numero ** 0.5
    return round(resultado,decimal)
