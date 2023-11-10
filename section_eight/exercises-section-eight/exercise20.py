"""
Faca um algoritmo que receba um numero inteiro positivo n e calcule o seu fatorioal, n!
"""


def fatorial(n):
    i = n
    fat = 1
    while i >= 1:
        fat = fat * i
        i = i - 1

    return fat


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro: '))

        if numero > 0:
            loop = False
            print(f'{numero}! = {fatorial(numero)}')

except ValueError:
    print('FORMATO INVALIDO!')
