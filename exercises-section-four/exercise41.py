"""
Faca um programa que leia o valor da hora de trabalho (em reais) e numero de horas
trabalhadas no mes. Imprima o valor a ser pago ao funcionario, adicionando 10% sobre
o valor calculado.
"""
try:
    valor_hora_trabalho = float(input('Informe o valor da hora de trabalho - R$ '))
    numero_horas_trabalhadas_mes = int(input('Informe numero de horas trabalhadas no mes: '))

    salario = (valor_hora_trabalho * numero_horas_trabalhadas_mes) * 1.10
    print(f'Salario Mensal: R$ {salario}')
except ValueError:
    print('O valor informado esta incorreto!')
