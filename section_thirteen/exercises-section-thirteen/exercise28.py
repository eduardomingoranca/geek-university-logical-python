"""
Faca um programa que recebe como entrada o nome de um arquivo de entrada e o nome
de um arquivo de saida. Cada linha do arquivo de entrada possui colunas de tamanho
de 30 caracteres. No arquivo de saida devera ser escrito o arquivo de entrada de
forma inversa.
"""

text_open = open('files/text_open.txt').read()

with open('files/text_exit.txt', 'w') as file:
    file.write(text_open[::-1])
