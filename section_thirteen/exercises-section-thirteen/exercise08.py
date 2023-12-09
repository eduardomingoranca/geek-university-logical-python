"""
Faca um programa que leia o conteudo de um arquivo e crie um arquivo com o mesmo
conteudo, mas com todas as letras minusculas convertidas para maiusculas. Os nomes
dos arquivos serao fornecidos, via teclado, pelo usuario. A funcao que converte
maiuscula para minuscula eh o toUpper(). Ela eh aplicada em cada caractere da string.
"""

names = open('files/names.txt').read()

with open('files/names_to_upper.txt', 'w') as file:
    for i in names:
        file.write(i.upper())


print(open('files/names_to_upper.txt').read())
