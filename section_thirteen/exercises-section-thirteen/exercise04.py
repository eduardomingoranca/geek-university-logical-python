"""
Faca um programa que receba do usuario um arquivo texto e mostre na tela quantas
letras sao vogais e quantos sao consoantes.
"""

file = open('files/arq.txt').read()

vowel = 0
consonant = 0
for i in file.split('\n'):
    if i == 'a' or i == 'o' or i == 'i' or i == 'u':
        vowel = vowel + 1
    else:
        consonant = consonant + 1

print(f'O arquivo arq.txt possui {vowel} vogal(is) e {consonant} consoantes.')
