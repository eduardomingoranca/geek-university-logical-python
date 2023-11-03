"""
Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos sao da forma:
A[i][j] = 2i + 7j - 2 se i < j
A[i][j] = 3i² - 1 se i == j
A[i][j] = 4i³ - 5j² se i > j
"""
a = [[0 for i in range(10)] for j in range(10)]

for linha in range(10):
    for coluna in range(10):
        if linha < coluna:
            a[linha][coluna] = 2 * linha + 7 * coluna - 2
        elif linha == coluna:
            a[linha][coluna] = pow(3 * linha, 2) - 1
        else:
            a[linha][coluna] = pow(4 * linha, 3) - pow(5 * coluna, 2)

for linha in range(10):
    for coluna in range(10):
        print(f'{a[linha][coluna]}', end=' ')
    print()
