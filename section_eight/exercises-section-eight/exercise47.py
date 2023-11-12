"""
Faca uma funcao que receba uma matriz 4 x 4 e retorne quantos valores maiores do que
10 ela possui.
"""


def quantidade_maior():
    qtd_maior = 0
    for lnh in range(4):
        for clna in range(4):
            if matriz[lnh][clna] > 10:
                qtd_maior = qtd_maior + 1

    return qtd_maior


try:
    matriz = [[0 for i in range(4)] for j in range(4)]

    for linha in range(4):
        for coluna in range(4):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    print(f'Existe {quantidade_maior()} valores maiores que 10.')
except ValueError:
    print('FORMATO INVALIDO!')
