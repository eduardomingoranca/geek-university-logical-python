"""
Faca um programa que receba do usuario um arquivo texto e um caracter. Mostre na tela
quantas vezes aquele caractere ocorre dentro do arquivo.
"""

file = open('files/names.txt').read()

caracter = input('Informe o caractere: ')

count = 0
for i in file:
    if i == caracter:
        count = count + 1

if count == 0:
    print(f'O caractere {caracter} nao existe no arquivo names.txt')
else:
    print(f'O caractere {caracter} ocorre {count} vez(es) no arquivo names.txt')
