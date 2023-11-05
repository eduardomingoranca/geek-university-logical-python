"""
Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva
o numero de alunos cuja pior nota foi na prova 1, o numero de alunos cuja pior nota
foi na prova 2, e o numero de alunos cuja pior nota foi na prova 3. Em caso de empate
das piores notas de um aluno, o criterio de desempate eh arbitrario, mas o aluno deve
ser contabilizado apenas uma vez.
"""
try:
    respostas = [[0 for i in range(3)] for j in range(10)]
    pior_nota_prova_um = 0
    pior_nota_prova_dois = 0
    pior_nota_prova_tres = 0

    print('INFORME AS RESPOSTAS DOS ALUNOS')
    for linha in range(10):
        for coluna in range(3):
            resposta = float(input(f'RESPOSTA[{linha}][{coluna}]: '))
            respostas[linha][coluna] = resposta

    print('')
    for linha in range(10):
        for coluna in range(3):
            print(f'{respostas[linha][coluna]}', end=' ')
        print('')

    for linha in range(10):
        for coluna in range(3):
            if min(respostas[linha]) == respostas[linha][coluna]:
                if coluna == 0:
                    pior_nota_prova_um = pior_nota_prova_um + 1
                elif coluna == 1:
                    pior_nota_prova_dois = pior_nota_prova_dois + 1
                elif coluna == 2:
                    pior_nota_prova_tres = pior_nota_prova_tres + 1

    print('')
    print(f'Numero de alunos cuja pior nota foi na prova 1: {pior_nota_prova_um}')
    print(f'Numero de alunos cuja pior nota foi na prova 2: {pior_nota_prova_dois}')
    print(f'Numero de alunos cuja pior nota foi na prova 3: {pior_nota_prova_tres}')

except ValueError:
    print('FORMATO INVALIDO!')
