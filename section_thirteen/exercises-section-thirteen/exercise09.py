"""
Faca um programa que receba dois arquivos do usuario, e crie um terceiro arquivo com
o conteudo dos dois primeiros juntos (o conteudo do primeiro seguido do conteudo do
segundo).
"""

names = open('files/names.txt').read()
names_women = open('files/names_women.txt').read()

with open('files/bible_names.txt', 'w') as file:
    for i in names:
        file.write(i)

    for j in names_women:
        file.write(j)

print(open('files/bible_names.txt').read())
