"""
Faca uma funcao que receba um numero N e retorne a soma dos algarismos de N!
"""


def soma_algarismos(numero):
    a = fatorial(numero) // 10
    b = fatorial(numero) % 10

    return f'{numero}!: {fatorial(numero)} | logarismos: {a} + {b} = {(a + b)}'


def fatorial(a):
    f = 1
    i = 1
    while i <= a:
        f = f * i
        i = i + 1

    return f


try:
    n = int(input('Informe um numero inteiro: '))

    print(f'{soma_algarismos(n)}')
except ValueError:
    print('FORMATO INVALIDO!')
