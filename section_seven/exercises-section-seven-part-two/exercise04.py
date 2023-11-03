"""
Leia uma matriz 4 x 4, imprima a matriz e retorne a localizacao (linha e a coluna) do
maior valor.
"""
try:
    matriz = [[0 for i in range(4)] for j in range(4)]

    maior_linha = 0
    maior_coluna = 0
    maior_valor_linha = 0
    maior_valor_coluna = 0
    for linha in range(4):
        for coluna in range(4):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

            if matriz[linha][coluna] > maior_valor_linha:
                maior_valor_linha = matriz[linha][coluna]
                maior_linha = linha
            if matriz[linha][coluna] > maior_valor_coluna:
                maior_valor_coluna = matriz[linha][coluna]
                maior_coluna = coluna

    for linha in range(4):
        for coluna in range(4):
            print(f'{matriz[linha][coluna]}', end=' ')
        print()

    print(f'LOCALIZACAO [{maior_linha}][{maior_coluna}] DO MAIOR VALOR!')
except ValueError:
    print('FORMATO INVALIDO!')
