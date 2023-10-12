"""
Leia um angulo em graus e apresente-o convertido em radianos. A formula de conversao
eh: R = G * pi / 180, sendo G o angulo em graus e R em radianos e pi = 3.14.
"""
import math

try:
    g = float(input('Informe um angulo em graus: '))
    r = math.pi * 180
    print(f'R = {g} / 180')
    print(f'R = {r:.2f}')
except ValueError:
    print('O valor informado esta invalido!')