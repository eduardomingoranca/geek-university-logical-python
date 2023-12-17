"""
Escreva um programa que leia a profissao e o tempo de servico (em anos) de cada um
dos 5 funcionarios de uma empresa e armazene-os no arquivo 'emp.txt'. Cada linha
do arquivo corresponde aos dados de um funcionario.
"""

with open('files/emp.txt', 'w') as file:
    i = 0
    while i < 5:
        profissao = input('Informe o nome da profissao: ')
        tempo_servico = float(input('Informe o tempo de servico (em anos): '))
        file.write(profissao + ', ' + str(tempo_servico))
        file.write('\n')
        i = i + 1
