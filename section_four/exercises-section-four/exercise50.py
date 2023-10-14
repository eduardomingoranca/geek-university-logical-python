"""
Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual.
"""
try:
    idade = int(input('Informe a idade: '))

    print(f'{idade} anos, ano atual {2023}, ano de nascimento {2023-idade}')
except ValueError:
    print('O valor informado esta invalido!')
