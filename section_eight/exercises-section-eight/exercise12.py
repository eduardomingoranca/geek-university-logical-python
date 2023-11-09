"""
Escreva uma funcao que receba um numero inteiro maior do que zero e retorne a soma
de todos os seus algarismos.
"""


def soma_algarismos(n):
    return (n // 100.0) + (n % 100.0 // 10.0) + (n % 100.0 % 10.0)


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro (entre 100 e 999): '))

        if 100 <= numero <= 999:
            loop = False
            print(f'S = {numero}')
            print(f'S = {numero // 100.0} + {numero % 100.0 // 10.0} + {numero % 100.0 % 10.0}')
            print(f'S = {soma_algarismos(numero)}')

except ValueError:
    print('FORMATO INVALIDO!')
