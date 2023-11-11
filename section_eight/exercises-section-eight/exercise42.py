"""
Faca uma funcao que receba um vetor de reais e retorne a media dele.
"""


def media(v, a):
    soma = 0
    for i in v:
        soma = soma + i

    return soma / a


try:
    loop = True
    vet = []
    j = 1
    while loop:
        numero = int(input(f'Informe {j}º numero positivo: '))

        if numero <= 0:
            loop = False
            print(f'Media = {media(vet, j-1)}')

        vet.append(numero)
        j = j + 1

except ValueError:
    print('FORMATO INVALIDO!')
