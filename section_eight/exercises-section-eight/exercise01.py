"""
Crie uma funcao que recebe como parametro um numero inteiro e devolve o seu dobro.
"""


def dobro(n):
    return pow(n, 2.0)


try:
    numero = int(input('Informe um numero inteiro: '))

    print(f'{numero} | {dobro(numero)}')
except ValueError:
    print('FORMATO INVALIDO!')
