"""
Faca um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A²
"""
try:
    a = [[0 for i in range(3)] for j in range(3)]
    b = [[0 for i in range(3)] for j in range(3)]

    for linha in range(3):
        for coluna in range(3):
            m = float(input(f'A[{linha}][{coluna}]: '))
            a[linha][coluna] = m

    for linha in range(3):
        for coluna in range(3):
            b[linha][coluna] = pow(a[linha][coluna], 2.0)

    for linha in range(3):
        for coluna in range(3):
            print(f'{a[linha][coluna]}', end=' ')
        print('')

    print(' ')
    for linha in range(3):
        for coluna in range(3):
            print(f'{b[linha][coluna]}', end=' ')
        print('')

except ValueError:
    print('FORMATO INVALIDO!')
