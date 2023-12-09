"""
Faca um programa que permita que o usuario entre com diversos nomes e telefone para
cadastro, e crie um arquivo com essas informacoes, uma por linha. O usuario finaliza
a entrada com '0' para o telefone.
"""

with open('files/phone.txt', 'w') as file:
    while True:
        caractere = input('Informe o nome e telefone ou digite 0 para sair: ')
        if caractere != '0':
            file.write(caractere)
            file.write('\n')
        else:
            break

print(open('files/phone.txt').read())
