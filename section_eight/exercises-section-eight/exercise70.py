"""
Um racional eh qualquer numero da forma p/q, sendo p inteiro e q inteiro nao nulo. Eh
conveniente representar um racional por um registro:

    struct racional {
        int p, q;
    }

Vamos convencionar que o campo q de todo racional eh estritamente positivo e que o
maximo divisor comum dos campos p e q eh 1. Escreva:
(a) uma funcao reduz que receba inteiros a e b e devolva o racional que representa a/b;
(b) uma funcao neg que receba um racional x e devolva o racional -x;
(c) uma funcao soma que receba racionais x e y e devolva o racional que representa a
    soma de x e y;
(d) uma funcao mult que receba racionais x e y e devolva o racional que representa o
    produto de x por y;
(e) uma funcao div que receba racionais x e y e devolva o racional que representa o
    quociente de x por y;
"""


def reduz(c, g):
    s = 0
    s1 = 0
    if c > g:
        i = c
        while i >= g:
            if c % i == 0 and g % i == 0:
                s = i
            i = i - 1
        return f'{c// s} / {g // s}'
    elif g > c:
        j = g
        while j >= c:
            if c % j == 0 and g % j == 0:
                s1 = j
            j = j - 1
        return f'{c// s1} / {g // s1}'


def neg(f):
    return -f


def soma(c, d):
    return c + d


def mult(c, d):
    return c * d


def div(c, d):
    return c // d


try:
    loop = True
    while loop:
        p = int(input('Informe um numero inteiro: '))
        q = int(input('Informe outro numero inteiro: '))

        if q != 0:
            loop = False
            a = p
            b = q
            x = p
            y = q
            print(f'REDUZ: {reduz(a, b)}')
            print(f'NEG: {neg(x)}')
            print(f'SOMA: {soma(x, y)}')
            print(f'MULT: {mult(x, y)}')
            print(f'DIV: {div(x, y)}')

except ValueError:
    print('FORMATO INVALIDO!')
