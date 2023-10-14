"""
Faca um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
    - O numero digitado ao quadrado
    - A raiz quadrada do numero digitado
"""
import math

try:
    loop = True
    while loop:
        numero = float(input('Informe um numero: '))

        if numero > 0:
            loop = False
            print(f'{numero}² = {pow(numero, 2)}')
            print(f'\/{numero} = {math.sqrt(numero):.2f}')

except ValueError:
    print('O valor informado esta invalido!')
