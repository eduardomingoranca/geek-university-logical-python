"""
Faca uma funcao para calcular o numero neperiano usando uma serie. A funcao deve
ter como parametro o numero de termos que serao somados (note que, quanto maior o
numero, mais proximo a resposta estara do valor e).

l = ∑ ∞ n=0 1   = 1  +  1   +  1  +  1   +  1  + ...
            n!    0!    1!     2!    3!     4!
"""


def neperiano(numero):
    l = 1
    i = 0
    while i <= numero:
        l = l + fatorial(i)
        i = i + 1

    return l


def fatorial(a):
    f = 1
    i = 1
    while i <= a:
        f = f * i
        i = i + 1

    return f


try:
    n = float(input('Informe um numero: '))

    print(f'l = {neperiano(n)}')
except ValueError:
    print('FORMATO INVALIDO!')
