"""
Faca um programa para corrigir uma prova com 10 questoes de multipla escolha (a, b,
c, d ou e), em uma turma com 3 alunos. Cada questao vale 1 ponto. Leia o gabarito, e
para cada aluno leia sua matricula (numero inteiro) e suas respostas. Calcule e escreva:
Para cada aluno, escreva sua matricula, suas respostas, e sua nota. O percentual de
aprovacao, assumindo media 7.0
"""
try:
    respostas_alunos = [[0 for i in range(10)] for j in range(3)]
    pontuacao_primeiro_aluno = 0
    pontuacao_segundo_aluno = 0
    pontuacao_terceiro_aluno = 0
    gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
    matricula = [0 for i in range(3)]
    notas = [0 for j in range(3)]
    aprovados = 0

    print('INFORME AS RESPOSTAS DOS ALUNOS [a, b, c, d, e]')
    for linha in range(3):
        for coluna in range(10):
            respostas = input(f'RESPOSTAS[{linha}][{coluna}]: ')
            respostas_alunos[linha][coluna] = respostas

    for linha in range(3):
        matriculas = int(input(f'Informe a matricula do {linha}º aluno: '))
        matricula[linha] = matriculas

    for linha in range(3):
        for coluna in range(10):
            if linha == 0:
                if respostas_alunos[linha][coluna] == gabarito[coluna]:
                    pontuacao_primeiro_aluno = pontuacao_primeiro_aluno + 1
            elif linha == 1:
                if respostas_alunos[linha][coluna] == gabarito[coluna]:
                    pontuacao_segundo_aluno = pontuacao_segundo_aluno + 1
            elif linha == 2:
                if respostas_alunos[linha][coluna] == gabarito[coluna]:
                    pontuacao_terceiro_aluno = pontuacao_terceiro_aluno + 1

    for i in range(3):
        if i == 0:
            notas[i] = pontuacao_primeiro_aluno
        elif i == 1:
            notas[i] = pontuacao_segundo_aluno
        elif i == 2:
            notas[i] = pontuacao_terceiro_aluno

    print('| NOTAS DOS ALUNOS |')
    for i in range(3):
        if i == 0:
            if notas[i] >= 7.0:
                print(f'NOTA: {notas[i]} | MATRICULA ALUNO: {matricula[i]} | APROVADO!')
                aprovados = aprovados + 1
            else:
                print(f'NOTA: {notas[i]} | MATRICULA ALUNO: {matricula[i]} | REPROVADO!')
        if i == 1:
            if notas[i] >= 7.0:
                print(f'NOTA: {notas[i]} | MATRICULA ALUNO: {matricula[i]} | APROVADO!')
                aprovados = aprovados + 1
            else:
                print(f'NOTA: {notas[i]} | MATRICULA ALUNO: {matricula[i]} | REPROVADO!')
        if i == 2:
            if notas[i] >= 7.0:
                print(f'NOTA: {notas[i]} | MATRICULA ALUNO: {matricula[i]} | APROVADO!')
                aprovados = aprovados + 1
            else:
                print(f'NOTA: {notas[i]} | MATRICULA ALUNO: {matricula[i]} | REPROVADO!')

    print(f'Percentual de aprovacao {(aprovados / 3) * 100}%')
except ValueError:
    print('FORMATO INVALIDO!')
