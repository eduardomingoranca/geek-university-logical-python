"""
Faca um algaritmo que receba um numero inteiro positivo n e calcule o somatorio de 1
ate n.
"""


def somatoria(numero):
    i = 1
    soma = 0
    while i <= numero:
        soma = soma + i
        i = i + 1

    return soma


try:
    loop = True
    while loop:
        n = int(input('Informe um numero inteiro: '))

        if n > 0:
            loop = False
            print(f'O somatorio de 1 ate {n} eh {somatoria(n)}')

except ValueError:
    print('FORMATO INVALIDO!')
