"""
Faca um programa gerenciar uma agenda de contatos. Para cada contato armazene o
nome, o telefone e o aniversario (dia e mes). O programa deve permitir
    (a) inserir contato
    (b) listar todos os contatos
"""

with open('files/phonebook.txt', 'w') as file:
    while True:
        nome = input('Informe o nome do contato: ')
        telefone = int(input('Informe o numero do telefone: '))
        aniversario = input('Informe o aniversario do contato (dd/MM): ')

        file.write(nome + ' ' + str(telefone) + ' ' + aniversario)
        file.write('\n')

        opcao = input('Deseja continuar? (s/n) ')
        if opcao == 'n' or opcao == 'N':
            break

print('Lista de todos os contatos: ' + open('files/phonebook.txt').read())