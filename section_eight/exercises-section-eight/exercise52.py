"""
Escreva uma funcao que recebe uma matriz quadrada de ordem N e calcule a sua
transposta (se B eh a matriz transposta de A entao aij = bij).
"""


def transposta(p, vet):
    for lnh in range(p):
        for clna in range(p):
            print(vet[clna][lnh], end=' ')
        print()


try:
    n = int(input('Informe o tamanho da matriz: '))
    a = [[0 for i in range(n)] for j in range(n)]

    for linha in range(n):
        for coluna in range(n):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            a[linha][coluna] = numero

    transposta(n, a)
except ValueError:
    print('FORMATO INVALIDO!')
