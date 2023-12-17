"""
Crie um programa que declare uma classe para o cadastro de alunos.
    (a) Deverao ser armazenados, para cada aluno: matricula, sobrenome (apenas um), e
        ano de nascimento.
    (b) Ao inicio do programa, o usuario devera informar o numero de alunos que serao
        armazenados
    (c) O programa devera pedir ao usuario que entre com as informacoes dos alunos
    (d) Em seguida, essas informacoes deverao ser gravadas em um arquivo
"""

with open('files/student_registration.txt', 'w') as file:
    quantidade_armazenada = int(input('Informe a quantidade de alunos que serao armazenados: '))

    i = 0
    while i < quantidade_armazenada:
        matricula = int(input(f'Informe o numero da matricula do {i+1}º aluno: '))
        sobrenome = input(f'Informe o sobrenome do {i+1}º aluno: ')
        ano_nascimento = int(input(f'Informe o ano de nascimento do {i+1}º aluno: '))

        file.write(str(matricula) + ' ' + sobrenome + ' ' + str(ano_nascimento))
        file.write('\n')
        i = i + 1
