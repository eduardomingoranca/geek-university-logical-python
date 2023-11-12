"""
Faca uma funcao que recebe, por parametro, uma matriz A[3][3] e retorna a soma dos
elementos da sua diagonal principal e da sua diagonal secundaria
"""


def soma_diagonais(p):
    soma = 0
    soma2 = 0
    for lnh in range(3):
        for clna in range(3):
            if lnh == clna:
                soma = soma + p[lnh][clna]
            elif lnh + clna == len(p) - 1:
                soma2 = soma2 + p[lnh][clna]

    return soma + soma2


try:
    a = [[0 for i in range(3)] for j in range(3)]

    for linha in range(3):
        for coluna in range(3):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            a[linha][coluna] = numero

    print(f'Soma: {soma_diagonais(a)}')
except ValueError:
    print('FORMATO INVALIDO!')
