"""
Faca uma funcao nao recursiva que receba um numero inteiro positivo n e retorne o
hiperfatorial desse numero. O hiperfatorial de um numero n, escrito H(n), eh definido por:
    H(n) = Πⁿ k = 1 k[k] = 1 * 2² * 3³ ... (n - 1)ⁿ-1 * nⁿ
"""


def hiperfatorial(n):
    i = 1
    h = 1
    while i <= n:
        h = h * int(pow(i, i))
        i = i + 1

    return h


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro: '))

        if numero > 0:
            loop = False
            print(f'H({numero}): {hiperfatorial(numero)}')

except ValueError:
    print('FORMATO INVALIDO!')
