"""
Leia o salario de um funcionario. Calcule e imprima o valor do novo salario, sabendo que
ele recebeu um aumento de 25%.
"""
try:
    salario = float(input('Salario de R$ '))
    salario *= 1.25
    print(f'R$ {salario} salario com reajuste de 25%')
except ValueError:
    print('O valor informado esta incorreto!')
