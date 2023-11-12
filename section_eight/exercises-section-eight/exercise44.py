"""
Faca uma funcao que receba como parametro um vetor X da 30 elementos inteiros e
retorne, tambem por parametro, dois vetores A e B. O vetor A deve conter os elementos
pares de X e o vetor B, os elementos impares.
"""


def pares_impares(vet):
    a = []
    b = []
    for j in vet:
        if j % 2 == 0:
            a.append(j)
        else:
            b.append(j)

    for k in a:
        print(k, end=' ')

    print(' ')
    for p in b:
        print(p, end=' ')


try:
    loop = True
    i = 1
    x = []
    while loop:
        n = int(input(f'Informe {i}º numero inteiro: '))
        x.append(n)

        if i == 30:
            loop = False
            pares_impares(x)
        i = i + 1
except ValueError:
    print('FORMATO INVALIDO!')
