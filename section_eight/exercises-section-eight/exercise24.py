"""
Escreva uma funcao que gera um triangulo de altura e lados n e base 2*n-1. Por exemplo,
a saida para n = 6 seria:
                               *
                             * * *
                           * * * * *
                         * * * * * * *
                       * * * * * * * * *
                      * * * * * * * * * *
"""


def triangulo(numero):
    i = 1
    while i <= numero:
        total = 2 * i - 1
        if total == 1:
            print('*')
        else:
            j = 1
            while j < total:
                print('*', end=' ')
                j = j + 1
            print('*')
        i = i + 1


try:
    loop = True
    while loop:
        n = int(input('Informe um numero inteiro: '))

        if n > 0:
            loop = False
            triangulo(n)

except ValueError:
    print('FORMATO INVALIDO!')