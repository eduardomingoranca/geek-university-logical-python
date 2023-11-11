"""
Faca uma funcao que receba um vetor de inteiros e retorne o maior valor.
"""


def maior_valor(v):
    return max(v)


try:
    loop = True
    vet = []
    j = 1
    while loop:
        numero = int(input(f'Informe {j}º numero inteiro positivo: '))
        vet.append(numero)

        if numero <= 0:
            loop = False
            print(f'Maior valor {maior_valor(vet)}')

        j = j + 1

except ValueError:
    print('FORMATO INVALIDO!')
