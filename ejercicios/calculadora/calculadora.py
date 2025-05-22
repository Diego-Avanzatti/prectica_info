from ejercicios.calculadora.operaciones import sumar, restar, multiplicar, dividir, potenciar, raiz_cuadrada

print("\nCALCULADORA\n")

def operacion_elegida(operacion,num_1,num_2 = None):
    if operacion == 1:
        resultado = sumar(num_1,num_2)
        print(f"{num_1} + {num_2} = {resultado}")
    elif operacion == 2:
        resultado = restar(num_1,num_2)
        print(f"{num_1} - {num_2} = {resultado}")
    elif operacion == 3:
        resultado = multiplicar(num_1,num_2)
        print(f"{num_1} x {num_2} = {resultado}")
    elif operacion == 4:
        if num_2 == 0:
            print("No se puede dividir por cero.")
        else:
            resultado = dividir(num_1,num_2)
            print(f"{num_1} / {num_2} = {resultado}")
    elif operacion == 5:
        resultado = potenciar(num_1,num_2)
        print(f"{num_1} ^ {num_2} = {resultado}")
    elif operacion == 6:
        resultado = raiz_cuadrada(num_1)
        print(f"\/{num_1} = {resultado}")
    

        

while True:
    entrada = input("Si desea iniciar la calculadora presione 's' y para salir 'n': ").lower()

    if entrada == "n":
        break 
    elif entrada == "s": 
        print("Seleccinar operacion:\n1-sumar\n2-restar\n3-multiplicar\n4-dividir\n5-potencia\n6-raiz cuadrada")

        seleccion = int(input("ingrese la opcion (1-6) ==> "))
        if seleccion > 6 or seleccion < 1:
            print("valor incorrecto.")
        else:
            num_1 = float(input("numero 1: "))

            if seleccion in [1,2,3,4,5]:
                num_2 = float(input("numero 2: "))
                operacion_elegida(seleccion,num_1,num_2)
            else:
                operacion_elegida(seleccion,num_1)
    else:
        print("Entrada incorrecta, presione 's' para iniciar o 'n' para salir.")
    

                