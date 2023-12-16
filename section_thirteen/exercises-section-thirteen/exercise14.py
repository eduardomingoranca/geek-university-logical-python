"""
Dado um arquivo contendo um conjunto de nome e data de nascimento (DD/MM/AAAA,
isto eh, 3 inteiros em sequencia), faca um programa que leia o nome do arquivo
e a data de hoje e construa outro arquivo contendo o nome e a idade de cada pessoa
do primeiro arquivo.
"""

names_dates = open('files/names_dates.txt').read()

with open('files/names_ages.txt', 'w') as file:
    file.write(names_dates[slice(0, 13)])
    file.write('\n')
    file.write(names_dates[slice(27, 43)])
    file.write(names_dates[slice(56, 71)])
    file.write('\n')

    i = 21
    while i < len(names_dates):
        age = 2023 - int(names_dates[slice(i, i + 4)])
        file.write(str(age))
        file.write('\n')
        i = i + 30
