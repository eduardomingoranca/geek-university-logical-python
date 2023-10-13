"""
Sejam a e b os catetos de um triangulo, onde a hipotenusa eh obtida pela equadracao:
hipotenusa = \/a² + b². Faca um programa que receba os valores de a e b e calcule
o valor da hipotenusa atraves da equacao. Imprima o resultado dessa operacao.
"""
import math

try:
    a = float(input('A: '))
    b = float(input('B: '))
    hipotenusa = math.sqrt(pow(a, 2) + pow(b, 2))
    print(f'hipotenusa = \/{a}² + {b}²')
    print(f'hipotenusa = {hipotenusa:.2f}')
except ValueError:
    print('O valor informado esta incorreto!')
