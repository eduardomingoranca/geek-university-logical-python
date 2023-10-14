"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular eh calculado por meio da seguinte formula: V = π * raio² * altura,
onde π = 3.141592
"""
import math

try:
    raio = float(input('raio: '))
    altura = float(input('altura: '))

    v = math.pi * pow(raio, 2) * altura
    print(f'V = {math.pi:.6f} * {raio}² * {altura}')
    print(f'V = {v:.2f}')
except ValueError:
    print('O valor informado esta incorreto!')
