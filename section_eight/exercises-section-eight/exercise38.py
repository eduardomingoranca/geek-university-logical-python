"""
Faca uma funcao nao recursiva que receba um numero inteiro positivo n e retorne o
fatorial exponencial desse numero. Um fatorial exponencial eh um inteiro positivo n
elevado a potencia de n - 1, que por sua vez eh elevado a potencia de n - 2 e assim
em diante.
Ou seja:  n(n-1)(n-2)...
"""


def fatorial_exponencial(n):
    i = 1
    fat_exp = 1
    while i <= n:
        fat_exp = fat_exp * int(pow(n, (n - i)))
        i = i + 1

    return fat_exp


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero positivo: '))

        if numero > 0:
            loop = False
            print(f'fatorial exponencial: {fatorial_exponencial(numero)}')

except ValueError:
    print('FORMATO INVALIDO!')
