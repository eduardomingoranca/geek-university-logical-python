"""
Faca um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes
informacoes sobre alunos de uma disciplina, sendo todas as informacoes do tipo inteiro:
    <> Primeira coluna: numero de matricula (use um inteiro)
    <> Segunda coluna: media das provas
    <> Terceira coluna: media dos trabalhos
    <> Quarta coluna: nota final
Elabore um programa que:

(a) Leia as tres primeiras informacoes de cada aluno
(b) Calcule a nota final como sendo a soma da media das provas e da media dos
    trabalhos
(c) Imprima a matricula do aluno que obteve a maior nota final (assuma que so existe
    uma maior nota)
(d) Imprima a media aritmetica das notas finais
"""
try:
    matriz = [[0 for i in range(4)] for j in range(5)]
    numero_matricula = 0
    media_provas = 0
    media_trabalhos = 0
    soma_nota = 0
    maior_nota = 0

    for linha in range(5):
        for coluna in range(4):
            if coluna == 0:
                numero_matricula = int(input(f'MATRICULA[{linha}][{coluna}]: '))
                matriz[linha][coluna] = numero_matricula
            elif coluna == 1:
                media_provas = float(input(f'MEDIA PROVAS[{linha}][{coluna}]: '))
                matriz[linha][coluna] = media_provas
            elif coluna == 2:
                media_trabalhos = float(input(f'MEDIA TRABALHOS[{linha}][{coluna}]: '))
                matriz[linha][coluna] = media_trabalhos
            elif coluna == 3:
                nota_final = media_provas + media_trabalhos
                matriz[linha][coluna] = nota_final

    for linha in range(5):
        for coluna in range(4):
            print(f'{matriz[linha][coluna]}', end=' ')
        print()

    for linha in range(5):
        for coluna in range(4):
            if coluna == 3:
                soma_nota = soma_nota + matriz[linha][coluna]
                if max(matriz[linha]) == matriz[linha][coluna]:
                    maior_nota = linha

    print(' ')
    print(f'MEDIA ARITMETICA DAS NOTAS: {soma_nota/5.0} | MATRICULA DA MAIOR NOTA: {maior_nota}')

except ValueError:
    print('FORMATO INVALIDO!')
