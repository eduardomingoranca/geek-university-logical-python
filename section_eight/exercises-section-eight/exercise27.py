"""
Faca uma funcao que receba como parametro o valor de um angulo em graus e calcule
o valor do seno desse angulo usando sua respectiva serie de Taylor:
    sen x = ∑ ∞ n=0 (-1)ⁿ   x2ⁿ + 1 = x = x³  +  x5 = ... para todo x,
                  (2n + 1)!              3!     5!
onde x eh o valor do angulo em radianos. Considerar π = 3.141593 e n variando de 0
ate 5.
"""
import math


def seno(a):
    count = 0
    p1 = 1
    p2 = 3
    soma_positiva = 0.0
    soma_negativa = 0.0

    while count <= 5:
        soma_positiva = soma_positiva + pow(a, p1) / fatorial(p1)
        p1 = p1 + 5

        soma_negativa = soma_negativa - pow(a, p2) / fatorial(p2)
        p2 = p2 + 5

        count = count + 1

    return soma_positiva + soma_negativa


def fatorial(a):
    f = 1
    i = 1
    while i <= a:
        f = f * i
        i = i + 1

    return f


try:
    angulo_graus = float(input('Informe o angulo em graus: '))

    print(f'Sen ({angulo_graus}): {seno(angulo_graus * math.pi / 180.0)}')
except ValueError:
    print('FORMATO INVALIDO!')
