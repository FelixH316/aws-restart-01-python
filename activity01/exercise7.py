"""
AWS re/Start

Activity:       Python 1
Author:         Felix Armenta
File:           exercise7.py
Description:    This script let you play rock, paper, scissors
"""


import tkinter as tk
import random


def determinar_ganador(eleccion_usuario):
    opciones = ['Piedra', 'Papel', 'Tijera']
    eleccion_pc = random.choice(opciones)
    
    # Lógica del juego
    if eleccion_usuario == eleccion_pc:
        resultado = "¡Es un empate! 😐"
    elif (eleccion_usuario == 'Piedra' and eleccion_pc == 'Tijera') or \
         (eleccion_usuario == 'Papel' and eleccion_pc == 'Piedra') or \
         (eleccion_usuario == 'Tijera' and eleccion_pc == 'Papel'):
        resultado = "¡Ganaste! :D"
    else:
        resultado = "¡La computadora gana! u_U"
        
    # Actualizar la interfaz con el resultado
    label_resultado.config(text=f"Computadora eligió: {eleccion_pc}\n\n{resultado}")

# 1. Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("350x250")
ventana.config(padx=20, pady=20)

# 2. Etiqueta de instrucciones
label_instruccion = tk.Label(ventana, text="Elige tu jugada:", font=("Arial", 14))
label_instruccion.pack(pady=10)

# 3. Contenedor (Frame) para alinear los botones horizontalmente
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# 4. Botones de opciones pasando el argumento con lambda
btn_piedra = tk.Button(frame_botones, text="[X] Piedra", width=10, command=lambda: determinar_ganador('Piedra'))
btn_piedra.grid(row=0, column=0, padx=5)

btn_papel = tk.Button(frame_botones, text="((() Papel", width=10, command=lambda: determinar_ganador('Papel'))
btn_papel.grid(row=0, column=1, padx=5)

btn_tijera = tk.Button(frame_botones, text="✂️ Tijera", width=10, command=lambda: determinar_ganador('Tijera'))
btn_tijera.grid(row=0, column=2, padx=5)

# 5. Etiqueta para mostrar quién ganó
label_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"), fg="#333333")
label_resultado.pack(pady=20)

# 6. Ciclo de ejecución de la ventana
ventana.mainloop()
