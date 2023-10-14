"""
Leia o valor do raio de um circulo e calcule e imprima a area do circulo correspondente.
A area do circulo eh π * raio², considere π = 3.141592
"""
import math

try:
    raio = float(input('Informe o valor do raio de um circulo: '))
    area = math.pi * pow(raio, 2)
    print(f'A = {math.pi:.6f} * {pow(raio, 2)}')
    print(f'A = {area:.2f}')
except ValueError:
    print('O valor informado esta incorreto!')
