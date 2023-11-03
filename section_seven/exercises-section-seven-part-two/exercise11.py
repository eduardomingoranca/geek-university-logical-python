"""
Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estao na diagonal
secundaria
"""
try:
    matriz = [[0 for i in range(3)] for j in range(3)]
    soma_diagonal_secundaria = 0

    for linha in range(3):
        for coluna in range(3):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    for linha in range(3):
        for coluna in range(3):
            if linha + coluna == len(matriz) - 1:
                soma_diagonal_secundaria = (soma_diagonal_secundaria
                                            + matriz[linha][coluna])

    print(f'Soma dos elementos que estao na diagonal secundaria: {soma_diagonal_secundaria}')
except ValueError:
    print('FORMATO INVALIDO!')
