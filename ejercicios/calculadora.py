from operaciones import suma, resta, multiplicacion, division

print("\nCALCULADORA\n")

def operacion_elegida(operacion,num_1,num_2):
    match operacion:
        case 1:
            sumar = suma(num_1,num_2)
            print(f"{num_1} + {num_2} = {sumar}")
        case 2:
            restar = resta(num_1,num_2)
            print(f"{num_1} - {num_2} = {restar}")
        case 3:
            multiplicar = multiplicacion(num_1,num_2)
            print(f"{num_1} x {num_2} = {multiplicar}")
        case 4:
            dividir = division(num_1,num_2)
            print(f"{num_1} % {num_2} = {dividir}")

while True:
    entrada = input("Si desea iniciar la calculadora presione 's' y para salir 'n': ").lower()

    if entrada == "n":
        break 
    elif entrada == "s": 
        print("Seleccinar operacion:\n1-sumar\n2-restar\n3-multiplicar\n4-dividir\n")

        seleccion = int(input("ingrese la opcion (1-4) ==> "))
        num_1 = float(input("numero 1: "))
        num_2 = float(input("numero 2: "))

        operacion_elegida(seleccion,num_1,num_2)
    else:
        print("Entrada incorrecta, presione 's' para iniciar o 'n' para salir.")
    

                