import tkinter as tk
from tkinter import ttk
from funciones import *

def convertir():
    try:
        valor = float(entrada_valor.get())
        opcion= combo_opcion.get()

        if opcion == "Kilómetros a millas":
            resultado = km_a_milla(valor)
        elif opcion == "Millas a kilómetros":
            resultado = milla_a_km(valor)
        elif opcion == "Celsius a Fahrenheit":
            resultado = celsius_a_fahrenheit(valor)
        elif opcion == "Fahrenheit a Celsius":
            resultado = fahrenheit_a_celsius(valor)
        elif opcion == "Kilogramos a libras":
            resultado = kg_a_libras(valor)
        elif opcion == "Libras a kilogramos":
            resultado = libras_a_kg(valor)
        else:
            resultado_label.config(text = "Seleccione una opción válida.",font=20)
            return
        resultado_label.config(text=f"Resultado: {resultado:.2f}",font=20)
    except ValueError:
        resultado_label.config(text="Ingrese un numero válido",font=20)


ventana = tk.Tk()
ventana.title("Conversor de unidades")
ventana.geometry("300x300")


etiqueta = tk.Label(ventana, text="Valor a convertir: ",font=("roboto",14))
etiqueta.pack(pady=10)

entrada_valor = tk.Entry(ventana,font=("Arial", 12))
entrada_valor.pack(pady=10)

opciones = ["Kilómetros a millas", "Millas a kilómetros", "Celsius a Fahrenheit", "Fahrenheit a Celsius", "Kilogramos a libras", "Libras a kilogramos" ]

combo_opcion = ttk.Combobox(ventana, values=opciones, state="readonly", font=16)
combo_opcion.pack(pady=10)

boton = tk.Button(ventana, text="Convertir", font=('roboto', 18), command= convertir)
boton.pack(pady=10)

resultado_label = tk.Label(ventana, text="Resultado: ")
resultado_label.pack(pady=10)

ventana.mainloop()