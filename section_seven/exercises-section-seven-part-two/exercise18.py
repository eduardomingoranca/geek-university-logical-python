"""
Faca um programa que permita ao usuario entrar com uma matriz de 3 x 3 numeros
inteiros. Em seguida, gere um array unidimensional pela soma dos numeros de cada
coluna da matriz e mostrar na tela esse array.
"""
try:
    matriz = [[0 for i in range(3)] for j in range(3)]
    soma_coluna = []
    soma1 = 0
    soma2 = 0
    soma3 = 0

    print('INFORME APENAS NUMEROS INTEIROS!')
    for linha in range(3):
        for coluna in range(3):
            numeros = int(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numeros

    for linha in range(3):
        for coluna in range(3):
            print(f'{matriz[linha][coluna]}', end=' ')
        print('')

    for linha in range(3):
        for coluna in range(3):
            if coluna == 0:
                soma1 = soma1 + matriz[linha][coluna]
            elif coluna == 1:
                soma2 = soma2 + matriz[linha][coluna]
            elif coluna == 2:
                soma3 = soma3 + matriz[linha][coluna]

    for linha in range(3):
        soma_coluna.append(soma1)
        soma_coluna.append(soma2)
        soma_coluna.append(soma3)
        break

    print('')
    for i in soma_coluna:
        print(i, end=' ')

except ValueError:
    print('FORMATO INVALIDO!')
