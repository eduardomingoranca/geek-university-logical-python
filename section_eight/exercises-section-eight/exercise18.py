"""
Faca uma funcao que receba por parametro dois valores X e Z. Calcule e retorne o
resultado de X ao quadrado de Z para o programa principal.
"""


def exponenciacao(x, z):
    return pow(x, z)


try:
    a = float(input('A: '))
    n = float(input('N: '))

    print(f'aⁿ = {exponenciacao(a, n)}')
except ValueError:
    print('FORMATO INVALIDO!')
