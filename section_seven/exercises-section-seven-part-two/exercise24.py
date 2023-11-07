"""
Na matriz de 20 x 20 abaixo, quatro numeros ao longo de uma linha diagonal foram
marcadas em negrito. O produto desses numeros eh 26 * 63 * 78 * 14 = 1788696.
Qual eh o maior produto de quatro numeros adjacentos em qualquer direcao (cima, baixo,
esquerda, direita, ou na diagonal) na matriz de 20 x 20?
"""
try:
    matriz = [[0 for i in range(20)] for j in range(20)]
    maior_produto = 1
    count = 1

    for linha in range(20):
        for coluna in range(20):
            m = float(input(f'MATRIZ[{linha}][{coluna}]: '))
            matriz[linha][coluna] = m

    for linha in range(20):
        for coluna in range(20):
            if coluna > 3 and linha < 17:
                produto = (matriz[linha][coluna] * matriz[linha+1][coluna-1] *
                           matriz[linha+2][coluna-2] * matriz[linha+3][coluna-3])
                if produto > maior_produto:
                    maior_produto = produto
            if coluna < 17:
                produto = (matriz[linha][coluna] * matriz[linha][coluna+1] *
                           matriz[linha][coluna+2] * matriz[linha][coluna+3])
                if produto > maior_produto:
                    maior_produto = produto
            if coluna < 17 and linha < 17:
                produto = (matriz[linha][coluna] * matriz[linha+1][coluna+1] *
                           matriz[linha][coluna+2] * matriz[linha][coluna+3])
                if produto > maior_produto:
                    maior_produto = produto

    print('')
    print(f'MAIOR PRODUTO: {maior_produto}')

except ValueError:
    print('FORMATO INVALIDO!')
