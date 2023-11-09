"""
Sejam a e b os catetos de um triangulo, onde a hipotenusa eh obtida pela equacao:
hipotenusa = √a² + b². Faca uma funcao que receba os valores de a e b e calcule o
valor da hipotenusa atraves da equacao.
"""
import math


def hipotenusa(a, b):
    return math.sqrt(pow(a, 2) + pow(b, 2))


try:
    x = float(input('A: '))
    y = float(input('B: '))

    print(f'hipotenusa = √{x}² + {y}²')
    print(f'hipotenusa = {hipotenusa(x, y)}')
except ValueError:
    print('FORMATO INVALIDO!')
