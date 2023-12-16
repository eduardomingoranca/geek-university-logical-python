"""
Faca um programa que recebe um vetor de 10 numeros, converta cada um desses
numeros para binario e grave a sequencia de 0s e 1s em um arquivo texto. Cada
numero deve ser gravado em uma linha.
"""

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open('files/binaries.txt', 'w') as file:
    y = 0
    while y < len(list_number):
        if y % 2 == 0:
            file.write(str(1))
            file.write('\n')
        else:
            file.write(str(0))
            file.write('\n')
        y = y + 1
