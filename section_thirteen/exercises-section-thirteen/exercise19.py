"""
Faca um programa que receba do usuario um arquivo que contenha o nome e a nota de
diversos alunos (da seguinte forma: NOME: JOAO NOTA: 8), um aluno por linha. Mostre
na tela o nome e a nota do aluno que possui a maior nota.
"""

grade = open('files/grade.txt').read()


i = 32
bigger = 0.0
while i < len(grade):
    if float(grade[slice(i, i + 3)]) > bigger:
        bigger = float(grade[slice(i, i + 3)])
    i = i + 36

print('Highest grade: '.__add__(str(bigger)))
