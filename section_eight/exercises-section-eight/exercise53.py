"""
Faca uma funcao que verifica se uma matriz quadrada de ordem N eh a matriz identidade.
"""


def identidade(m, p):
    for lnh in range(p):
        for clna in range(p):
            if lnh == clna:
                m[lnh][clna] = 1
            else:
                m[lnh][clna] = 0

    for lnh in range(p):
        for clna in range(p):
            print(f'{m[lnh][clna]}', end=' ')
        print()


try:
    n = int(input('Informe o tamanho da matriz: '))
    a = [[0 for i in range(n)] for j in range(n)]

    for linha in range(n):
        for coluna in range(n):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            a[linha][coluna] = numero

    identidade(a, n)
except ValueError:
    print('FORMATO INVALIDO!')

