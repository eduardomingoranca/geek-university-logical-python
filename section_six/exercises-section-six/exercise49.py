"""
O funcionario chamado Carlos tem um colega chamado Joao que recebe um salario que
equivale a um terco do seu salario. Carlos gosta de fazer aplicacoes na caderneta de
poupanca e vai aplicar seu salario integralmente nela, pois esta rendendo 2% ao mes.
Joao aplicara seu salario integralmente no fundo de renda fixa, que esta rendendo 5%
ao mes. Construa um programa que devera calcular e mostrar a quantidade de meses
necessarios para que o valor pertencente a Joao iguale ou ultrapasse o valor pertencente
a Carlos.
"""
try:
    salario_carlos = float(input('Informe o salario de Carlos - R$ '))

    salario_joao = salario_carlos / 3.0
    meses = 0
    while salario_carlos > salario_joao:
        salario_carlos = salario_carlos * 1.02
        salario_joao = salario_joao * 1.05

        meses = meses + 1

    print(f'{meses} MESES')

except ValueError:
    print('O formato de valor informado esta invalido!')
