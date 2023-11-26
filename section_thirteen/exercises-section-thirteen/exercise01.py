"""
Escreva um programa que:
    (a) Crie/abra um arquivo texto de nome 'arq.txt'
    (b) Permita que o usuario grave diversos caracteres nesse arquivo, ate que o usuario
        entre com o caractere '0'
    (c) Feche o arquivo
Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres
armazenados.
"""

with open('files/arq.txt', 'w') as arquivo:
    while True:
        caractere = input('Informe um caractere ou digite 0 para sair: ')
        if caractere != '0':
            arquivo.write(caractere)
            arquivo.write('\n')
        else:
            break

print(open('files/arq.txt').read())
