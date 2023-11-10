"""
Faca uma funcao que receba dois numeros inteiros positivos por parametro e retorne a
soma dos N numeros inteiros existentes entre eles.
"""


def soma_intervalo(n1, n2):
    soma = 0
    if n1 < n2:
        i = n1
        while i <= n2:
            soma = soma + i
            i = i + 1
    elif n1 > n2:
        i = n2
        while i <= n1:
            soma = soma + i
            i = i + 1

    return soma


try:
    loop = True
    while loop:
        a = int(input('Informe o 1º numero: '))
        b = int(input('Informe o 2º numero: '))

        if a != b:
            loop = False
            print(f'SOMA: {soma_intervalo(a, b)}')
except ValueError:
    print('FORMATO INVALIDO!')
