"""
Faca uma funcao que receba uma matriz de 3 x 3 elementos. Calcule a soma dos
elementos que estao acima da diagonal principal.
"""


def soma_acima_diagonal_principal(m):
    soma = 0
    for lnh in range(3):
        for clna in range(3):
            if lnh < clna:
                soma = soma + m[lnh][clna]

    return soma


try:
    matriz = [[0 for i in range(3)] for j in range(3)]

    for linha in range(3):
        for coluna in range(3):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    print(f'Soma acima da diagonal principal: {soma_acima_diagonal_principal(matriz)}')
except ValueError:
    print('FORMATO INVALIDO!')
