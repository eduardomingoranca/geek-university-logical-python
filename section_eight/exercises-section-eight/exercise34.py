"""
Faca uma funcao nao recursiva que receba um numero inteiro positivo impar N e retorne
o fatorial duplo desse numero. O fatorial duplo eh definido como o produto de todos os
numeros naturais impares de 1 ate algum numero natural impar N. Assim, o fatorial duplo
de 5 eh: 5! = 1 * 3 * 5 = 15
"""


def fatorial_duplo(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 2

    return f


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro: '))

        if numero > 0:
            loop = False
            print(f'{numero}!: {fatorial_duplo(numero)}')

except ValueError:
    print('FORMATO INVALIDO!')
