"""
Foi realizada uma pesquisa de algumas caracteristicas fisicas de cinco habitantes de certa
regiao. De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos (A - Azuis
ou C - Castanhos), cor dos cabelos (L - Louros, P - Pretos ou C - Castanhos) e idade.
    <> Faca uma funcao que leia esses dados em um vetor.
    <> Faca uma funcao que determine a media de idade das pessoas com olhos castanhos
       e cabelos pretos.
    <> Faca uma funcao que determine e devolva ao programa principal a maior idade
       entre os habitantes.
    <> Faca uma funcao que determine e devolva ao programa principal a quantidade de
       individuos do sexo feminino cuja idade esta entre 18 e 35 (inclusive) e que tenham
       olhos azuis e cabelos louros.
"""


def dados_habitantes(sex, eyes, hairs, ages):
    print()
    for s in sex:
        print(f'{s}', end=' ')

    print()
    for e in eyes:
        print(f'{e}', end=' ')

    print()
    for h in hairs:
        print(f'{h}', end=' ')

    print()
    for a in ages:
        print(f'{a}', end=' ')


def media_idade(eyes, hairs, ages):
    soma = 0
    j = 0
    k = 0

    while k < len(ages):
        if eyes[k] == 'C':
            if hairs[k] == 'P':
                soma = soma + ages[k]
                j = j + 1
        k = k + 1

    if soma == 0 or j == 0:
        return 0

    return soma / j


def maior_idade(ages):
    maior = 0
    for m in ages:
        if m > maior:
            maior = m

    return maior


def quantidade_feminino(sex, eyes, hairs, ages):
    quantidade = 0
    j = 0

    while j < len(sex):
        if sex[j] == 'F':
            if 18 <= ages[j] <= 35:
                if eyes[j] == 'A':
                    if hairs[j] == 'L':
                        quantidade = quantidade + 1
        j = j + 1

    return quantidade


try:
    sexos = []
    cor_olhos = []
    cor_cabelos = []
    idades = []
    loop = True
    i = 1

    while loop:
        sexos.append(input(f'Informe o sexo do {i}º habitante [M / F]: '))
        cor_olhos.append(input(f'Informe a cor dos olhos do {i}º habitante [A / C]: '))
        cor_cabelos.append(input(f'Informe a cor dos cabelos do {i}º habitante [L / P / C]: '))
        idades.append(int(input(f'Informe a idade do {i}º habitante: ')))

        if i == 5:
            loop = False
            dados_habitantes(sexos, cor_olhos, cor_cabelos, idades)
            print(f'\nMedia de idade das pessoas com olhos castanhos e cabelos pretos: '
                  f'{media_idade(cor_olhos, cor_cabelos, idades)}')
            print(f'Maior idade entre os habitantes: {maior_idade(idades)}')
            print(f'A quantidade de individuos do sexo feminino cuja idade esta entre 18 e 35 (inclusive) e que tenham '
                  f'olhos azuis e cabelos louros: {quantidade_feminino(sexos, cor_olhos, cor_cabelos, idades)}')

        i = i + 1
except ValueError:
    print('FORMATO INVALIDO!')
