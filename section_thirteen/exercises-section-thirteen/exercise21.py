"""
Crie um programa que receba como entrada o numero de alunos de uma disciplina. Aloque
dinamicamente em uma estrutura para armazenar as informacoes a respeito desses
alunos: nome do aluno e sua nota final. Use nomes com o maximo 40 caracteres. Em
seguida, salve os dados dos alunos em um arquivo binario. Por fim, leia o arquivo e
mostre o nome do aluno com a maior nota.
"""

grade = open('files/grade.txt').read()


i = 32
bigger = 0.0
while i < len(grade):
    if float(grade[slice(i, i + 3)]) > bigger:
        bigger = float(grade[slice(i, i + 3)])
    i = i + 36

print('Highest grade: '.__add__(str(bigger)))
