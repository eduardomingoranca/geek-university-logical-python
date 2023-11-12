"""
Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""
try:
    matriz = [[0 for i in range(4)] for j in range(4)]
    quantidade_maior = 0

    for linha in range(4):
        for coluna in range(4):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    for linha in range(4):
        for coluna in range(4):
            if matriz[linha][coluna] > 10:
                quantidade_maior = quantidade_maior + 1

    print(f'Existe {quantidade_maior} valores maiores que 10.')
except ValueError:
    print('FORMATO INVALIDO!')
