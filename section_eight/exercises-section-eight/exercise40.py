"""
Faca uma funcao que receba um vetor de inteiros e retorne quantos valores pares ele
possui.
"""


def total_pares(v):
    pares = 0
    for i in v:
        if i % 2 == 0:
            pares = pares + 1

    return pares


try:
    loop = True
    vet = []
    j = 1
    while loop:
        numero = int(input(f'Informe {j}º numero positivo: '))

        if numero <= 0:
            loop = False
            print(f'Existe {total_pares(vet)} valores pares!')

        vet.append(numero)
        j = j + 1

except ValueError:
    print('FORMATO INVALIDO!')
