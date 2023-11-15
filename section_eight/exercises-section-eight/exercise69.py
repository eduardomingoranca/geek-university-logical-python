"""
Faca um programa que faca operacoes simples de fracoes:
    <> Crie e leia duas fracoes p e q, compostas por numerador e denominador.
    <> Encontre o maximo divisor comum entre o numerador e o denominador, e simplifique
       que as fracoes.
    <> Apresente a soma, a subtracao, o produto e o quociente entre as fracoes lidas.
Obs.: Cria uma funcao para cada item.
"""


def imprimir(a, a1, b, b1):
    return f'{a} / {a1} | {b} / {b1}'


def maximo_divisor_comum(c, c1):
    s = 0
    s1 = 0
    if c > c1:
        i = c
        while i >= c1:
            if c % i == 0 and c1 % i == 0:
                s = i
            i = i - 1
        return f'{c // s} / {c1 // s}'
    elif c1 > c:
        j = c1
        while j >= c:
            if c % j == 0 and c1 % j == 0:
                s1 = j
            j = j - 1
        return f'{c // s1} / {c1 // s1}'


def produto(a, b, a1, b1):
    if b == b1:
        return f'{a * a1} / {b}'
    else:
        return f'{a * a1} / {b * b1}'


def quociente(a, b, a1, b1):
    return f'{a * a1} / {b * b1}'


def soma(a, b, a1, b1):
    if b == b1:
        return f'{(a + a1)} / {b}'
    else:
        return f'{a * b1 + a1 * b} / {b * b1}'


def subtracao(a, b, a1, b1):
    if b == b1:
        return f'{(a - a1)} / {b}'
    else:
        return f'{a * b1 - a1 * b} / {b * b1}'


try:
    loop = True
    while loop:
        p = int(input('Informe o numerador da 1ª fracao: '))
        q = int(input('Informe o denominador da 1ª fracao: '))

        p1 = int(input('Informe o numerador da 2ª fracao: '))
        q1 = int(input('Informe o denominador da 2ª fracao: '))

        if p != 0 and p1 != 0 and q != 0 and q1 != 0:
            loop = False
            print()
            print(imprimir(p, q, p1, q1))
            print(f'PRODUTO: {produto(p, q, p1, q1)}')
            print(f'QUOCIENTE: {quociente(p, q, p1, q1)}')
            print(f'SOMA: {soma(p, q, p1, q1)}')
            print(f'SUBTRACAO: {subtracao(p, q, p1, q1)}')
            print(f'MDC: {maximo_divisor_comum(p, q)}')
            print(f'MDC2: {maximo_divisor_comum(p1, q1)}')

except ValueError:
    print('FORMATO INVALIDO!')
