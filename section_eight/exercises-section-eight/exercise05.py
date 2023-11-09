"""
Faca uma funcao e um programa de teste para o calculo do volume de uma esfera.
Sendo que o raio eh passao por parametro.
V = 4/3 * π * R³
"""
import math


def volume_esfera(r):
    return 4/3 * math.pi * pow(r, 3)


try:
    raio = float(input('Informe o raio de uma esfera: '))

    print(f'V: {volume_esfera(raio)}')
except ValueError:
    print('FORMATO INVALIDO!')
