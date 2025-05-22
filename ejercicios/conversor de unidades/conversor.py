from funciones import *

# def convertidor(unidades):
#     if eleccion == "1":
#         resultado = km_a_milla(unidades)
#         print(f"Los {unidades} km son igual a {resultado} millas.")
#     elif eleccion == "2":
#         resultado = milla_a_km(unidades)
#         print(f"Las {unidades} millas son igual a {resultado} km.")
#     elif eleccion == "3":
#         resultado = celsius_a_fahrenheit(unidades)
#         print(f"Los {unidades} °C son igual a {resultado} °F.")
#     elif eleccion == "4":
#         resultado = fahrenheit_a_celsius(unidades)
#         print(f"Los {unidades} °F son igual a {resultado} °C.")
#     elif eleccion == "5":
#         resultado = kg_a_libras(unidades)
#         print(f"Los {unidades} kg son igual a {resultado} libras.")
#     elif eleccion == "6":
#         resultado = libras_a_kg(unidades)
#         print(f"Los {unidades} libras son igual a {resultado} kg.")

while True:

    ingresar = input("\nSi desea realizar una conversion presione 's' iniciar, 'n' cerrar: ").lower()

    if ingresar == "n":
        break
    elif ingresar == "s":
        print("\n¿Qué desea convertir?")

        eleccion = input("\n1-Longitud.\n2-Temperatura.\n3-Peso.\n==> ")
        if eleccion == "1":
            opcion = input("\n1-Kilometros a millas.\n2-Millas a kilometros.\n==> ")
            if opcion == "1":
                print("\nKilometros a millas")
                kilometros = float(input("Ingrese los km: "))
                conversion = km_a_milla(kilometros)
                print(f"Los {kilometros}km equivalen a {conversion:.2f} millas")
            elif opcion == "2":
                print("\nMillas a kilometros")
                millas = float(input("Ingrese las millas: "))
                conversion = milla_a_km(millas)
                print(f"Las {millas}millas equivalen a {conversion:.2f} km")
            else:
                print("Incorrecto, ingrese un valor 1-2")
        elif eleccion == "2":
            opcion = input("\n1-Celsius a fahrenheit.\n2-Fahrenheit a Celsius.\n==> ")
            if opcion == "1":
                print("\nCelsius a fahrenheit")
                celsius = float(input("Ingrese los °C: "))
                conversion = celsius_a_fahrenheit(celsius)
                print(f"Los {celsius}°C equivalen a {conversion:.2f}°F")
            elif opcion == "2":
                print("\nFahrenheit a celsius")
                fahrenheit = float(input("Ingrese los °F: "))
                conversion = fahrenheit_a_celsius(fahrenheit)
                print(f"Los {fahrenheit}°F equivalen a {conversion:.2f}°C")
            else:
                print("Incorrecto, ingrese un valor 1-2")
        elif eleccion == "3":
            opcion = input("\n1-Kilogramos a libras.\n2-Libras a kilogramos.\n==> ")
            if opcion == "1":
                print("\nKilogramos a libras")
                kg = float(input("Ingrese los Kg: "))
                conversion = kg_a_libras(kg)
                print(f"Los {kg}Kg equivalen a {conversion:.2f} libras")
            elif opcion == "2":
                print("\nLibras a kilogramos")
                libras = float(input("Ingrese las libras: "))
                conversion = libras_a_kg(libras)
                print(f"Las {libras} libras equivalen a {conversion:.2f}kg")
            else:
                print("Incorrecto, ingrese un valor 1-2")
        else:
            print("ingrese un valor del 1-3")
    else:
        print("Ingrese un valor s-iniciar c-cerrar")




