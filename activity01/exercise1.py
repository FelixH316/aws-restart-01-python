"""
AWS re/Start

Activity:       Python 1
Author:         Felix Armenta
File:           exercise1.py
Description:    Using a function ask for name, last name, age (you
                could ask for any other datum) and then print
                everything on the screen.
"""


def get_user_data():
    """
    This functions gets user data and then it prints them
    """
    nombre = input("\n\tIngresa tu nombre: ")
    apellido = input("\tIngresa tu apellido: ")
    edad = int(input("\tIngresa tu edad: "))
    civil = input("\tIngresa tu estado civil: ")
    print(f"\n\tSaludos {nombre} {apellido} de {edad} años de edad, lamento que estes {civil}")


if __name__ == "__main__":
    get_user_data()
