"""
Abra um arquivo texto, calcule e escreva o numero de caracteres, o numero de linhas e
o numero de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre no
arquivo (ignorando letras com acento). Obs.: palavras sao separadas por um ou mais
caracteres espaco, tabulacao ou nova linha.
"""

names = open('files/names.txt').read()

line = 0
for i in names.split('\n'):
    if i != '':
        line = line + 1

character = 0
for j in names:
    if j != '\n':
        character = character + 1

word = 0
for p in names.split('\n'):
    if p != '':
        word = word + 1

print(f'O arquivo tem {character} caracteres, {line} linhas e {word} palavras')
