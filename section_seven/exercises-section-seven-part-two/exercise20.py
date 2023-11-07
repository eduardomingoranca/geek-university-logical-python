"""
Faca programa que leia uma matriz 3 x 6 com valores reais.
    (a) Imprima a soma de todos os elementos das colunas impares.
    (b) Imprima a media aritmetica dos elementos da segunda e quarta colunas.
    (c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
    (d) Imprima a matriz modificada.
"""
try:
    matriz = [[0 for i in range(6)] for j in range(3)]
    soma_coluna_impar = 0
    soma_colunas = 0

    for linha in range(3):
        for coluna in range(6):
            m = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = m

    for linha in range(3):
        for coluna in range(6):
            if coluna % 2 != 0:
                soma_coluna_impar = soma_coluna_impar + matriz[linha][coluna]
            if coluna == 1:
                soma_colunas = soma_colunas + matriz[linha][coluna]
            if coluna == 3:
                soma_colunas = soma_colunas + matriz[linha][coluna]
            if coluna == 5:
                matriz[linha][coluna] = matriz[linha][1] + matriz[linha][2]

    for linha in range(3):
        for coluna in range(6):
            print(f'{matriz[linha][coluna]}', end=' ')
        print()

    print('')
    print(f'Soma de todos os elementos das colunas impares: {soma_coluna_impar}')
    print(f'Media aritmetica dos elementos da segunda e quarta colunas: {soma_colunas / 6.0}')
except ValueError:
    print('FORMATO INVALIDO!')
