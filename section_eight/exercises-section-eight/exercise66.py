"""
Faca uma funcao que dado um caractere qualquer retorne o mesmo caractere sempre
em maiusculo.
"""


def toUpperCase(c):
    return c.upper()


try:
    caractere = input('Informe uma letra: ')

    print(f'{toUpperCase(caractere)}')
except ValueError:
    print('FORMATO INVALIDO!')
