"""
Crie um programa que receba como entrada o numero de uma disciplina.
Aloque dinamicamente dois vetores para armazenar as informacoes a
respeito desses alunos. O primeiro vetor contem o nome dos alunos e
o segundo contem suas notas finais. Crie um arquivo que armazene, a
cada linha, o nome do aluno e sua nota final. Use nomes com no maximo
40 caracteres, complete com espaco em branco.
"""

students = []
grades = []

for i in range(5):
    student = input('student name: ')
    grade = float(input('student grade: '))
    students.append(student)
    grades.append(grade)

with open('files/students_grades.txt', 'w') as file:
    for i in range(5):
        file.write(students[i] + ',' + str(grades[i]))
        file.write('\n')
