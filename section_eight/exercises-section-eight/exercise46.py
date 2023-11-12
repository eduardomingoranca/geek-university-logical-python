"""
Crie um programa contendo as seguintes funcoes que recebem um vetor V numeros reais
como parametros:
    <> Impressao normal do vetor.
    <> Impressao inversa
    <> Funcao que retorna a media aritmetica dos elementos do vetor.
"""


def impressao_vetores(vet):
    print('\n')
    for i in vet:
        print(f'{i}', end=' ')

    print()
    reverse = vet[::-1]
    for j in reverse:
        print(f'{j}', end=' ')


def media_aritmetica(vet):
    soma = 0
    for i in vet:
        soma = soma + i

    return soma / len(vet)


try:
    loop = True
    v = []
    while loop:
        n = float(input(f'Informe o numero positivo: '))

        if n < 0:
            loop = False
            impressao_vetores(v)
            print(f'\nMedia aritmetica dos elementos do vetor: {media_aritmetica(v)}')

        v.append(n)
except ValueError:
    print('FORMATO INVALIDO!')

