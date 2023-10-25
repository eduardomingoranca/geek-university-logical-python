"""
Faca um programa que leia um numero indeterminado de idades de individuos (pare
quando for informada a idade 0), e calcule a idade media desse grupo.
"""
try:
    soma = 0
    quantidade = 0
    loop = True
    while loop:
        print('Informe o valor ZERO para parar!')
        idade = int(input('Informe a idade: '))

        if idade == 0:
            loop = False
            print(f'MEDIA DAS IDADES: {soma / quantidade}')

        soma = soma + idade
        quantidade = quantidade + 1

except ValueError:
    print('O formato de valor informado esta invalido!')
