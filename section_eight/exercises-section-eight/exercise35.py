"""
Faca uma funcao nao recursiva que receba um numero positivo n e retorne o fatorial
quadruplo desse numero. O fatorial quadruplo de um numero n eh dado por:
    (2n)!
     n!
"""


def fatorial_quadruplo(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1

    f2 = 1
    j = 1
    a = 2 * n
    while j <= a:
        f2 = f2 * j
        j = j + 1

    return f2 / f


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro: '))

        if numero > 0:
            loop = False
            print(f'(2*{numero})! / {numero}!: {fatorial_quadruplo(numero)}')

except ValueError:
    print('FORMATO INVALIDO!')
