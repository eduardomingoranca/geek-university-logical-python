"""
Faca uma funcao que recebe, por parametro, uma matriz A[4][4] e retorna a soma dos
seus elementos.
"""


def soma(mat):
    soma_elementos = 0
    for lnh in range(4):
        for clna in range(4):
            soma_elementos = soma_elementos + mat[lnh][clna]

    return soma_elementos


try:
    a = [[0 for i in range(4)] for j in range(4)]

    for linha in range(4):
        for coluna in range(4):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            a[linha][coluna] = numero

    print(f'Soma: {soma(a)}')
except ValueError:
    print('FORMATO INVALIDO!')
