"""
Um funcionario recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996
recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem ao dobro
do ano anterior. Faca um programa que determine o salario atual do funcionario.
"""
anos = 1995
salario = 2000
while anos != 2023:
    salario = salario + pow(1.5, 2.0)
    anos = anos + 1

print(f'{anos} - R$ {salario}')
