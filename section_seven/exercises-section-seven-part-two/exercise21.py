"""
Faca um programa que leia duas matrizes 2 x 2 com valores reais. Ofereca ao usuario
um menu de opcoes:
    (a) somar as duas matrizes
    (b) subtrair a primeira matriz da segunda
    (c) adicionar uma constante as duas matrizes
    (d) imprimir as matrizes
Nas duas primeiras opcoes uma terceira matriz 3 x 3 deve ser criada. Na terceira opcao
o valor da constante deve ser lido e o resultado da adicao da constante deve ser armazenado
na propria matriz.
"""
try:
    m1 = [[0 for i in range(2)] for j in range(2)]
    m2 = [[0 for i in range(2)] for j in range(2)]
    soma = [[0 for i in range(3)] for j in range(3)]
    subtracao = [[0 for i in range(3)] for j in range(3)]

    for linha in range(2):
        for coluna in range(2):
            m = float(input(f'M1[{linha}][{coluna}]: '))
            m1[linha][coluna] = m

    for linha in range(2):
        for coluna in range(2):
            m = float(input(f'M2[{linha}][{coluna}]: '))
            m2[linha][coluna] = m

    for linha in range(2):
        for coluna in range(2):
            soma[linha][coluna] = m1[linha][coluna] + m2[linha][coluna]
            subtracao[linha][coluna] = m1[linha][coluna] - m2[linha][coluna]

    constante = float(input('Informe o valor de uma constante: '))

    for linha in range(2):
        for coluna in range(2):
            m1[linha][coluna] = m1[linha][coluna] + constante
            m2[linha][coluna] = m2[linha][coluna] + constante

    for linha in range(3):
        for coluna in range(3):
            print(f'{soma[linha][coluna]}', end=' ')
        print('')

    print(' ')
    for linha in range(3):
        for coluna in range(3):
            print(f'{subtracao[linha][coluna]}', end=' ')
        print('')

    print(' ')
    for linha in range(2):
        for coluna in range(2):
            print(f'{m1[linha][coluna]}', end=' ')
        print('')

    print(' ')
    for linha in range(2):
        for coluna in range(2):
            print(f'{m2[linha][coluna]}', end=' ')
        print('')

except ValueError:
    print('FORMATO INVALIDO!')
