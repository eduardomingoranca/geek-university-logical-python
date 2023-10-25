"""
Faca um programa que leia um conjunto nao determinado de valores, um de cada vez, e
escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize
a entrada de dados com um valor negativo ou zero.
"""
import math

try:
    loop = True
    while loop:
        print('Informe um valor NEGATIVO ou ZERO para finalizar.')
        n = float(input('N: '))

        if n < 0 or n == 0:
            loop = False
        else:
            print(f'{n}² = {pow(n, 2.0):.2f}')
            print(f'{n}³ = {pow(n, 3.0):.2f}')
            print(f'√{n} = {math.sqrt(n):.2f}')

except ValueError:
    print('O formato de valor informado esta invalido!')
