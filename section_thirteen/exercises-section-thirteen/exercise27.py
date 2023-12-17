"""
Faca um programa para gerenciar as notas dos alunos de uma turma salva em um arquivo.
O programa devera ter um menu contendo as seguintes opcoes:
    (a) Definir informacoes da turma;
    (b) Inserir aluno e notas;
    (c) Exibir alunos e medias;
    (d) Exibir alunos aprovados;
    (e) Exibir alunos reprovados;
    (f) Sair do programa (fim)
"""

count = 0.0
with open('files/manage_grades.txt', 'w') as file:
    while True:
        nome_aluno = input('Informe o nome do aluno: ')
        nota = float(input('Informe a nota do aluno: '))
        nota2 = float(input('Informe a segunda nota do aluno: '))

        file.write(nome_aluno + '   ' + str(nota) + ' ' + str(nota2))
        file.write('\n')

        count = count + 1
        opcao = input('Deseja continuar? (s/n) ')
        if opcao == 'n' or opcao == 'N':
            break

manage_grades = open('files/manage_grades.txt').read()

i = 0
while i < len(manage_grades):
    print(manage_grades[slice(i, i + 13)])
    n1 = float(manage_grades[slice(i + 16, i + 16 + 3)])
    n2 = float(manage_grades[slice(i + 20, i + 20 + 3)])

    media = (n1 + n2) / count
    print('MEDIA DAS NOTAS: ' + str(media))

    if media >= 7.0:
        print('APROVADO')
    else:
        print('REPROVADO')
    i = i + 24
