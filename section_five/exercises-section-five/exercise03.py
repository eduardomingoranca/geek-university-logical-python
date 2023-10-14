"""
Leia um numero real. Se o numero for positivo imprima a raiz quadrada. Do contrario,
imprima o numero ao quadrado.
"""
import math

try:
    numero = float(input('Informe um numero real: '))

    if numero > 0:
        print(f'\/{numero} = {math.sqrt(numero):.2f}')
    else:
        print(f'{numero}² = {pow(numero, 2)}')

except ValueError:
    print('O valor informado esta invalido!')
