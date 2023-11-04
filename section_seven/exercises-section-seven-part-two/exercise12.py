"""
Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.
"""
try:
    matriz = [[0 for i in range(3)] for j in range(3)]

    for linha in range(3):
        for coluna in range(3):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    for linha in range(3):
        for coluna in range(3):
            print(f'{matriz[coluna][linha]}', end=' ')
        print()

except ValueError:
    print('FORMATO INVALIDO!')
