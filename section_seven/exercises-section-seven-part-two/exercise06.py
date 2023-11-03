"""
Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posicao
das matrizes lidas.
"""
try:
    m1 = [[0 for i in range(4)] for j in range(4)]
    m2 = [[0 for i in range(4)] for j in range(4)]
    maior = [[0 for i in range(4)] for j in range(4)]

    for linha in range(4):
        for coluna in range(4):
            numero = float(input(f'M1[{linha}][{coluna}]: '))
            m1[linha][coluna] = numero

    for linha in range(4):
        for coluna in range(4):
            numero = float(input(f'M2[{linha}][{coluna}]: '))
            m2[linha][coluna] = numero

    for linha in range(4):
        for coluna in range(4):
            if m1[linha][coluna] > m2[linha][coluna]:
                maior[linha][coluna] = m1[linha][coluna]
            elif m2[linha][coluna] > m1[linha][coluna]:
                maior[linha][coluna] = m2[linha][coluna]
            else:
                maior[linha][coluna] = m1[linha][coluna]

    for linha in range(4):
        for coluna in range(4):
            print(f'{maior[linha][coluna]}', end=' ')
        print()

except ValueError:
    print('FORMATO INVALIDO!')
