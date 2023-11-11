"""
Faca uma funcao que receba como parametro o valor de um angulo em graus e calcule
o valor do cosseno desse angulo usando sua respectiva serie de Taylor:
    cos x = ∑ ∞ n=0 (-1)ⁿ    x2ⁿ = 1 = x² + x4 = ... para todo x,
                    (2n)!             2!   4!
onde x eh o valor do angulo em radianos. Considerar π = 3.141593 e n variando de 0
ate 5.
"""
import math


def cosseno(v):
    count = 0
    p1 = 2
    p2 = 4
    soma_positiva = 0.0
    soma_negativa = 0.0

    while count <= 5:
        soma_negativa = soma_negativa - pow(v, p1) / fatorial(p1)
        p1 = p1 + 5

        soma_positiva = soma_positiva + pow(v, p2) / fatorial(p2)
        p2 = p2 + 5

        count = count + 1

    return 1 + soma_positiva + soma_negativa


def fatorial(a):
    f = 1
    i = 1
    while i <= a:
        f = f * i
        i = i + 1

    return f


try:
    angulo_graus = float(input('Informe o angulo em graus: '))

    print(f'Cos({angulo_graus}): {cosseno(angulo_graus * math.pi / 180.0)}')
except ValueError:
    print('FORMATO INVALIDO!')
