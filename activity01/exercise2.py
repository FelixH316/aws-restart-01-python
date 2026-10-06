"""
AWS re/Start

Activity:       Python 1
Author:         Felix Armenta
File:           exercise2.py
Description:    Using a function ask any phrase and then print its
                lenght
"""


def get_phrase_lenght() -> int:
    """
    This function returns the lenght of any phrase

    Parameters:
        @str phrase: Any string

    Return:
        @int result: Lenght of the phrase
    """
    phrase = input("\n\tIngresa una frase: ")
    return len(phrase)


if __name__ == "__main__":
    caracteres = get_phrase_lenght()
    print(f"\n\tTu frase tiene {caracteres} caracteres")
