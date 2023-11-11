"""
Faca uma funcao nao recursiva que receba um numero inteiro positivo N e retorne o
superfatorial desse numero. O superfatorial de um numero N eh definida pelo produto dos
N primeiros fatoriais de N. Assim, o superfatorial de 4 eh sf(4) = 1! * 2! * 3! * 4! = 288
"""


def superfatorial(n):
    i = 1
    sf = 1
    j = 1
    f = 1
    while i <= n:
        while j <= i:
            f = f * j
            sf = sf * f
            j = j + 1
        i = i + 1

    return sf


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero positivo: '))

        if numero > 0:
            loop = False
            print(f'sf({numero}): {superfatorial(numero)}')

except ValueError:
    print('FORMATO INVALIDO!')
