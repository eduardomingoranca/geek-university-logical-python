"""
Faca uma funcao que receba um inteiro N como parametro, calcule e retorne o resultado
da seguinte serie:
    S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N + 3)
"""


def serie(numero):
    i = 1
    s = 0
    while i <= numero:
        s = s + (pow(i, 2) + 1) / (i + 3)
        i = i + 1

    return s


try:
    loop = True
    while loop:
        n = int(input('Informe um numero inteiro: '))

        if n > 0:
            loop = False
            print(f'S = {serie(n):.2f}')

except ValueError:
    print('FORMATO INVALIDO!')