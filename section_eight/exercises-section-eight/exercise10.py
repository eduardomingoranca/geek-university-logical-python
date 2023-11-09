"""
Faca uma funcao que receba dois numeros e retorne qual deles eh o maior.
"""


def maior(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2


try:
    loop = True
    while loop:
        a = float(input('Informe o 1º numero: '))
        b = float(input('Informe o 2º numero: '))

        if a != b:
            loop = False
            print(f'Maior = {maior(a, b)}')
except ValueError:
    print('FORMATO INVALIDO!')
