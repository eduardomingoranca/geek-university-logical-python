"""
Faca uma funcao que receba uma matriz 3 x 3 elementos. Calcule e retorne a soma
dos elementos que estao na diagonal secundaria.
"""


def soma_diagonal_secundaria(m):
    soma = 0
    for lnh in range(3):
        for clna in range(3):
            if lnh + clna == len(m) - 1:
                soma = soma + m[lnh][clna]

    return soma


try:
    matriz = [[0 for i in range(3)] for j in range(3)]

    for linha in range(3):
        for coluna in range(3):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    print(f'Soma da diagonal secundaria: {soma_diagonal_secundaria(matriz)}')
except ValueError:
    print('FORMATO INVALIDO!')
