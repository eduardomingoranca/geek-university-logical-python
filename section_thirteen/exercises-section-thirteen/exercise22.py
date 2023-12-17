"""
Faca um programa que recebe como entrada o nome de um arquivo de entrada e o nome
de um arquivo de saida. O arquivo de entrada contem o nome de um aluno ocupando 40
caracteres e tres inteiros que indicam suas notas. O programa devera ler o arquivo
de entrada e gerar um arquivo de saida onde aparece o nome do aluno e as suas notas
em ordem crescente.
"""

names_grades = open('files/names_grades.txt').read()

with open('files/ascending_order.txt', 'w') as file:
    i = 0
    while i < len(names_grades):
        file.write(names_grades[slice(i, i + 12)])
        file.write('\n')
        i = i + 28

    j = 16
    list_student_01 = []
    list_student_02 = []
    list_student_03 = []
    while j < len(names_grades):
        list_student_01.append(float(names_grades[slice(j, j + 3)]))
        list_student_02.append(float(names_grades[slice(j + 4, j + 7)]))
        list_student_03.append(float(names_grades[slice(j + 8, j + 11)]))
        j = j + 28

    list_student_01.sort()
    list_student_02.sort()
    list_student_03.sort()

    for p in list_student_01:
        file.write(str(p) + ' ')

    file.write('\n')
    for p in list_student_02:
        file.write(str(p) + ' ')

    file.write('\n')
    for p in list_student_03:
        file.write(str(p) + ' ')
