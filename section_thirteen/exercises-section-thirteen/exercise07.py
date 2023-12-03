"""
Faca um programa que receba do usuario um arquivo texto. Crie outro arquivo texto
contendo o texto arquivo de entrada, mas com as vogais substituidas por '*'.
"""

alphabet = open('files/alphabet.txt').read()

with open('files/update_alphabet.txt', 'w') as file:
    for i in alphabet:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            file.write('*')
        else:
            file.write(i)

print(open('files/update_alphabet.txt').read())
