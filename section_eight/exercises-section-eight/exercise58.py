"""
Faca uma funcao que receba, por parametro, duas matrizes quadradas de ordem N, A e
B, e retorna uma matriz C, tambem por parametro, que seja o produto matricial de A e B.
"""


def produto_matricial(v, p, num):
    c = [[0 for i in range(num)] for j in range(num)]

    for lnha in range(num):
        for clna in range(num):
            c[lnha][clna] = v[lnha][clna] + p[lnha][clna]

    for lnha in range(num):
        for clna in range(num):
            print(f'{c[lnha][clna]}', end=' ')
        print()


try:
    loop = True
    while loop:
        n = int(input('Ordem N: '))

        a = [[0 for i in range(n)] for j in range(n)]
        b = [[0 for i in range(n)] for j in range(n)]

        if n > 0:
            loop = False
            for linha in range(n):
                for coluna in range(n):
                    numero = float(input(f'A[{linha}][{coluna}]: '))
                    a[linha][coluna] = numero

            for linha in range(n):
                for coluna in range(n):
                    numero = float(input(f'A[{linha}][{coluna}]: '))
                    b[linha][coluna] = numero

            produto_matricial(a, b, n)

except ValueError:
    print('FORMATO INVALIDO!')
