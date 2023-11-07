"""
Faca um programa que leia duas matrizes A e B de tamanho 3 x 3 e calcule C = A * B
"""
try:
    a = [[0 for i in range(3)] for j in range(3)]
    b = [[0 for i in range(3)] for j in range(3)]
    c = [[0 for i in range(3)] for j in range(3)]

    for linha in range(3):
        for coluna in range(3):
            m = float(input(f'A[{linha}][{coluna}]: '))
            a[linha][coluna] = m

    for linha in range(3):
        for coluna in range(3):
            m = float(input(f'B[{linha}][{coluna}]: '))
            b[linha][coluna] = m

    for linha in range(3):
        for coluna in range(3):
            c[linha][coluna] = a[linha][coluna] * b[linha][coluna]

    for linha in range(3):
        for coluna in range(3):
            print(f'{c[linha][coluna]}', end=' ')
        print()

except ValueError:
    print('FORMATO INVALIDO!')
