"""
AWS re/Start

Activity:       Python 1
Author:         Felix Armenta
File:           exercise3.py
Description:    Using a function print a rhombus centered.
"""


def print_rhombus(rhomb_size: int) -> bool:
    """
    This functions prints a rhoumbus centered.
    Parameters:
        @int rhomb_size: The widht of your rhomb
    
    Return:
        @bool -: None if couldn't be printed
    """
    if rhomb_size == 0:
        print("Tu rombo no existe, como tu vida con ella")
        return None
    elif rhomb_size < 0:
        print("Tu rombo es imaginario, como tu felicidad")
        return None

    # Generar la mitad superior (incluyendo el centro)
    for i in range(rhomb_size):
        espacios = ' ' * (rhomb_size - i - 1)
        asteriscos = '*' * (2 * i + 1)
        print(espacios + asteriscos)
    
    # Generar la mitad inferior
    for i in range(rhomb_size - 2, -1, -1):
        espacios = ' ' * (rhomb_size - i - 1)
        asteriscos = '*' * (2 * i + 1)
        print(espacios + asteriscos)
    return True


if __name__ == "__main__":    
    rhomb_size = int(input("\nIngresa la altura de tu rombo (la base \
                           cuenta): "))
    print_rhombus(rhomb_size)
