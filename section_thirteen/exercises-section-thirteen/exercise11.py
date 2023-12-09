"""
Faca um programa no qual o usuario informa o nome do arquivo e uma palavra, e retorne
o numero de vezes que aquela palavra aparece no arquivo.
"""

animals = open('files/animals.txt').read()

p1 = slice(0, 3)
p2 = slice(4, 7)
p3 = slice(8, 11)

word = input('Informe uma palavra: ')

count = 0
if word == animals[p1]:
    count = count + 1

if word == animals[p2]:
    count = count + 1

if word == animals[p3]:
    count = count + 1


if count == 0:
    print(f'A palavra {word} nao existe no arquivo!')
else:
    print(f'A palavra {word} repete {count} vez(es) no arquivo')
