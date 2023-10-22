"""
Faca um programa que simula o lancamento de dois dados, d1 e d2, n vezes, e tem como
saida o numero de cada dado e a relacao entre eles (>, <, =) de cada lancamento.
"""
from random import randint


try:
    n = int(input('Informe a quantidade de lancamentos dos dados: '))

    contador = 0
    while contador < n:
        d1 = randint(1, 6)
        d2 = randint(1, 6)

        if d1 > d2:
            print(f'd1: {d1} | d2: {d2} || d1 maior')
        elif d2 > d1:
            print(f'd2: {d2} | d2: {d1} || d2 maior')
        else:
            print(f'd1: {d1} | d2: {d2} || d1 e d2 iguais')

        contador = contador + 1

except ValueError:
    print('O formato de valor informado esta invalido!')
