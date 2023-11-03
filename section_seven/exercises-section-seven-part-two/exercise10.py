"""
Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estao na diagonal
principal
"""
try:
    matriz = [[0 for i in range(3)] for j in range(3)]
    soma_diagonal_principal = 0

    for linha in range(3):
        for coluna in range(3):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    for linha in range(3):
        for coluna in range(3):
            if linha == coluna:
                soma_diagonal_principal = (soma_diagonal_principal
                                           + matriz[linha][coluna])

    print(f'Soma dos elementos que estao na diagonal principal: {soma_diagonal_principal}')
except ValueError:
    print('FORMATO INVALIDO!')
