"""
Faca um programa que receba como entrada o ano corrente e o nome de dois arquivos:
um de entrada e outro de saida. Cada linha do arquivo de entrada contem o nome de
uma pessoa (ocupando 40 caracteres) e o seu ano de nascimento. O programa devera
ler o arquivo de entrada e gerar um arquivo de saida onde aparece o nome da pessoa
seguida por uma string que representa a sua idade.
    <> Se a idade for menor do que 18 anos, escreva 'menor de idade'
    <> Se a idade for maior do que 18 anos, escreva 'maior de idade'
    <> Se a idade for igual a 18 anos, escreva 'entrando na maior idade'
"""

names_born_year = open('files/names_born_year.txt').read()

with open('files/names_age_group.txt', 'w') as file:
    i = 0
    while i < len(names_born_year):
        file.write(names_born_year[slice(i, i+16)])
        file.write('\n')
        i = i + 22

    y = 17
    while y < len(names_born_year):
        age = 2023 - int(names_born_year[slice(y, y + 4)])
        if age > 18:
            file.write('maior de idade')
            file.write('\n')
        elif age == 18:
            file.write('entrando na maior idade')
            file.write('\n')
        else:
            file.write('menor de idade')
            file.write('\n')
        y = y + 22
