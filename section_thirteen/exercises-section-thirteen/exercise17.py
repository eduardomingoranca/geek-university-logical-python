"""
Faca um programa que leia um arquivo que contenha as dimensoes de uma matriz (linha
e coluna), a quantidade de posicoes que serao anuladas, e as posicoes a serem anuladas
(linha e coluna). O programa le esse arquivo e, em seguida, produz um novo arquivo com
a matriz com as dimensoes dadas no arquivo lido, e todas as posicoes especificadas no
arquivo ZERADAS e o restante recebendo o valor 1.
"""

matrix = [[0 for i in range(3)] for j in range(3)]

with open('files/matriz.txt', 'w') as file:
    for line in range(3):
        for column in range(3):
            numero = int(input(f'M[{line}][{column}]: '))
            matrix[line][column] = numero
            file.write(str(matrix[line][column]) + " ")
        file.write('\n')

valor = int(input('Informe um numero da linha e coluna para remover: '))

with open('files/matriz_saida.txt', 'w') as f:
    for line in range(3):
        for column in range(3):
            if valor == line and valor == column:
                f.write('0' + ' ')
            else:
                f.write('1' + ' ')
        f.write('\n')
