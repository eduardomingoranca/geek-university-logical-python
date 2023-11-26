"""
Faca um programa que receba do usuario um arquivo texto e mostre na tela quantas
letras sao vogais.
"""

file = open('files/arq.txt').read()

count = 0
for i in file:
    if i == 'a' or i == 'o' or i == 'i' or i == 'u':
        count = count + 1

print(f'O arquivo arq.txt possui {count} vogal(is)')
