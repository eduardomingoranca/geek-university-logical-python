"""
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente
de um banco e retorne quantas notas de cada valor serao necessarias para atender ao
saque com a menor quantidade de notas possivel. Serao utilizadas notas de 100, 50,
20, 10, 5, 2 e 1 real.
"""
try:
    print('| Informe um valor MENOR ou IGUAL A ZERO para FINALIZAR! !')
    loop = True
    while loop:
        valor_saque = int(input('Informe o valor para o saque - R$ '))

        if valor_saque <= 0.0:
            loop = False
        else:
            notas_100 = valor_saque // 100
            notas_50 = valor_saque % 100 // 50
            notas_20 = valor_saque % 100 % 50 // 20
            notas_10 = valor_saque % 100 % 50 % 20 // 10
            notas_05 = valor_saque % 100 % 50 % 20 % 10 // 5
            notas_02 = valor_saque % 100 % 50 % 20 % 10 % 5 // 2
            notas_01 = valor_saque % 100 % 50 % 20 % 10 % 5 % 2 // 1

            print(f'VALOR SAQUE R$ {valor_saque}')
            print(f'NOTAS DE R$ 100.00: {notas_100}')
            print(f'NOTAS DE R$ 50.00: {notas_50}')
            print(f'NOTAS DE R$ 20.00: {notas_20}')
            print(f'NOTAS DE R$ 10.00: {notas_10}')
            print(f'NOTAS DE R$ 5.00: {notas_05}')
            print(f'NOTAS DE R$ 2.00: {notas_02}')
            print(f'NOTAS DE R$ 1.00: {notas_01}')

except ValueError:
    print('O formato de valor informado esta invalido!')
