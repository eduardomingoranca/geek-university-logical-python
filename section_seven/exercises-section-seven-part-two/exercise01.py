"""
Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""
try:
    matriz = [[0 for i in range(4)] for j in range(4)]

    for linha in range(4):
        for coluna in range(4):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    for linha in range(4):
        for coluna in range(4):
            print(f'{matriz[linha][coluna]:.2f}', end=' ')
        print()

except ValueError:
    print('FORMATO INVALIDO!')
