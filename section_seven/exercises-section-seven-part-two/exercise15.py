"""
Leia uma matriz 5 x 10 que se refere respostas de 10 questoes de multipla escolha,
referentes a 5 alunos. Leia tambem um vetor de 10 posicoes contendo o gabarito de
respostas que podem ser a, b, c ou d. Seu programa devera comparar as respostas
de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a
pontuacao correspondente a cada aluno.
"""
try:
    alunos = [[0 for i in range(10)] for j in range(5)]
    gabarito = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
    pontuacao_primeiro_aluno = 0
    pontuacao_segundo_aluno = 0
    pontuacao_terceiro_aluno = 0
    pontuacao_quarto_aluno = 0
    pontuacao_quinto_aluno = 0
    resultado = []

    print('INFORME AS RESPOSTAS DOS ALUNOS [a, b, c, d]')
    for linha in range(5):
        for coluna in range(10):
            respostas = input(f'M[{linha}][{coluna}]: ')
            alunos[linha][coluna] = respostas

    for linha in range(5):
        for coluna in range(10):
            if linha == 0:
                if alunos[linha][coluna] == gabarito[coluna]:
                    pontuacao_primeiro_aluno = pontuacao_primeiro_aluno + 1
            if linha == 1:
                if alunos[linha][coluna] == gabarito[coluna]:
                    pontuacao_segundo_aluno = pontuacao_segundo_aluno + 1
            if linha == 2:
                if alunos[linha][coluna] == gabarito[coluna]:
                    pontuacao_terceiro_aluno = pontuacao_terceiro_aluno + 1
            if linha == 3:
                if alunos[linha][coluna] == gabarito[coluna]:
                    pontuacao_quarto_aluno = pontuacao_quarto_aluno + 1
            if linha == 4:
                if alunos[linha][coluna] == gabarito[coluna]:
                    pontuacao_quinto_aluno = pontuacao_quinto_aluno + 1

    for i in range(10):
        if i == 0:
            resultado.append(pontuacao_primeiro_aluno)
        if i == 1:
            resultado.append(pontuacao_segundo_aluno)
        if i == 2:
            resultado.append(pontuacao_terceiro_aluno)
        if i == 3:
            resultado.append(pontuacao_quarto_aluno)
        if i == 4:
            resultado.append(pontuacao_quinto_aluno)

    for linha in range(5):
        for coluna in range(10):
            print(f'{alunos[linha][coluna]}', end=' ')
        print()

    print()
    print('RESULTADOS')
    for i in resultado:
        print(i, end=' ')

except ValueError:
    print('FORMATO INVALIDO!')
