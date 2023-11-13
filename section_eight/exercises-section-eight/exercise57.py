"""
Faca uma funcao que recebe, por parametro, uma matriz A[7][6] e uma coluna N e retorne
a soma dos elementos dessa coluna.
"""


def soma_coluna(numero, vet):
    soma = 0
    for lnha in range(7):
        for clna in range(6):
            if numero == clna:
                soma = soma + vet[lnha][clna]

    return soma


try:
    a = [[0 for i in range(6)] for j in range(7)]

    for linha in range(7):
        for coluna in range(6):
            num = float(input(f'A[{linha}][{coluna}]: '))
            a[linha][coluna] = num

    loop = True
    while loop:
        n = int(input('Informe a linha: '))

        if 0 <= n <= 6:
            loop = False
            print(f'Soma da coluna {n}: {soma_coluna(n, a)}')

except ValueError:
    print('FORMATO INVALIDO!')
