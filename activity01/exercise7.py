"""
AWS re/Start

Activity:       Python 1
Author:         Felix Armenta
File:           exercise7.py
Description:    This script let you play rock, paper, scissors against 
                skynet
"""
import tkinter as tk
import random
FONT = "Verdana"
FONT_SIZE = 12


def determinar_ganador(eleccion_usuario):
    """
    This functions receives a string with your selection to play
    rock, paper, scissors and then it displays the result with
    tkinter
    """
    opciones = ['Piedra', 'Papel', 'Tijera']
    eleccion_pc = random.choice(opciones)
    
    # Lógica del juego
    if eleccion_usuario == eleccion_pc:
        resultado = "¡Es un empate! 😐"
        color_resultado = "#5C9AFF" #Azul
    elif (eleccion_usuario == 'Piedra' and eleccion_pc == 'Tijera') or \
         (eleccion_usuario == 'Papel' and eleccion_pc == 'Piedra') or \
         (eleccion_usuario == 'Tijera' and eleccion_pc == 'Papel'):
        resultado = "¡Ganaste! :D"
        color_resultado = "#2F9923" # Verde
    else:
        resultado = "¡Skynet gana! u_U"
        color_resultado = "#DB0000" # Rojo
        
    # Actualizar la interfaz con el resultado
    label_resultado.config(text=f"Skynet eligió: {eleccion_pc}\n\n{resultado}",
                           font=("Arial", 16, "bold"),
                           fg=color_resultado)


if __name__ == "__main__":
    # 1. Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Piedra, Papel o Tijera")
    ventana.geometry("500x250")
    ventana.config(padx=20, pady=20) #bg="#2b2b2b")

    # 2. Etiqueta de instrucciones
    label_instruccion = tk.Label(ventana, text="ELIGE TU JUGADA:",
                                 font=(FONT, 14, "bold"),
                                 fg="#FF9900")
    label_instruccion.pack(pady=10)

    # 3. Contenedor (Frame) para alinear los botones horizontalmente
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    # 4. Botones de opciones pasando el argumento con lambda
    btn_piedra = tk.Button(frame_botones,
                           text="[X] Piedra",
                           font=(FONT, FONT_SIZE, "bold"),
                           width=10,
                           command=lambda: determinar_ganador('Piedra'))
    btn_piedra.grid(row=0, column=0, padx=5)

    btn_papel = tk.Button(frame_botones,
                          text="((() Papel",
                          font=(FONT, FONT_SIZE, "bold"),
                          width=10,
                          command=lambda: determinar_ganador('Papel'))
    btn_papel.grid(row=0, column=1, padx=5)

    btn_tijera = tk.Button(frame_botones,
                           text="✂️ Tijera",
                           font=(FONT, FONT_SIZE, "bold"),
                           width=10,
                           command=lambda: determinar_ganador('Tijera'))
    btn_tijera.grid(row=0, column=2, padx=5)

    # 5. Etiqueta para mostrar quién ganó
    label_resultado = tk.Label(ventana,
                               text="",
                               font=(FONT, FONT_SIZE, "bold")) #bg="#2b2b2b") 
    label_resultado.pack(pady=20)

    # 6. Ciclo de ejecución de la ventana
    ventana.mainloop()
