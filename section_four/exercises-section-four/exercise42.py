"""
Receba o salario-base de um funcionario. Calcule e imprima o salario a receber, sabendo-se
que esse funcionario tem uma gratificacao de 5% sobre o salario-base. Alem disso,
ele paga 7% de imposto sobre o salario-base.
"""
try:
    salario_base = float(input('salario-base R$ '))
    salario_receber = (salario_base * 1.05) - (salario_base * 0.07)
    print(f'salario a receber - R$ {salario_receber}')
except ValueError:
    print('O valor informado esta incorreto!')
