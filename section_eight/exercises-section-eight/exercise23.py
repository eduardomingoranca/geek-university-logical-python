"""
Escreva uma funcao que gera um triangulo lateral de altura 2*n-1 e n largura. Por exemplo,
a saida para n = 4 seria:
      *
      * *
      * * *
      * * * *
      * * *
      * *
      *
"""


def triangulo_lateral(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print('*', end=' ')
            j = j + 1
        print()
        i = i + 1

    k = n
    while k > 1:
        p = k
        while p > 1:
            print('*', end=' ')
            p = p - 1
        print()
        k = k - 1


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro: '))

        if numero > 0:
            loop = False
            triangulo_lateral(numero)

except ValueError:
    print('FORMATO INVALIDO!')
