"""
Faca uma funcao que receba a altura e o raio de um cilindro circular e retorne o volume
do cilindro. O volume de um cilindro circular eh calculado por meio da seguinte formula:
V = π * raio² * altura, onde π = 3.141592
"""
import math


def volume_cilindro(a, r):
    return math.pi * pow(r, 2) * a


try:
    altura = float(input('Informe a altura: '))
    raio = float(input('Informe o raio: '))

    print(f'V = {math.pi} * {pow(raio, 2)} * {altura}')
    print(f'V = {volume_cilindro(altura, raio)}')
except ValueError:
    print('FORMATO INVALIDO!')
