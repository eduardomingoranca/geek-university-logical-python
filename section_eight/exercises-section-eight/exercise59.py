"""
Faca uma funcao que rebece, por parametro, 2 vetores de 10 elementos inteiros e que
calcule e retorne, tambem por parametro, o vetor uniao dos dois primeiros
"""


def uniao_vetores(x, y):
    c = []

    for p in x:
        c.append(p)

    for k in y:
        c.append(k)

    uniao = set(c)
    for n in uniao:
        print(f'{n}', end=' ')


try:
    a = []
    b = []
    i = 0

    loop = True
    while loop:
        a.append(int(input(f'A[{i}]: ')))
        b.append(int(input(f'B[{i}]: ')))

        if i == 9:
            loop = False
            uniao_vetores(a, b)
        i = i + 1

except ValueError:
    print('FORMATO INVALIDO!')
