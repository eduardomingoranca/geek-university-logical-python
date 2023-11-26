"""
Faca um programa que receba do usuario um arquivo texto e mostre na tela quantas
linhas esse arquivo possui.
"""
linhas = open('files/arq.txt').read()

count = 0
for i in linhas.split():
    count = count + 1

print(f'O arquivo arq.txt possui {count} linhas')
