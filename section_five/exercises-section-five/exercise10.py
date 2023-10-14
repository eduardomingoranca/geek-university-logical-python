"""
Faca um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes formulas (onde h corresponde a altura):
    . Homens: (72.7 * h) - 58
    . Mulheres: (62.1 * h) - 44.7
"""
try:
    loop = True
    while loop:
        h = float(input('Informe a altura: '))
        s = input('Informe o sexo (m/f): ')

        if s == 'M' or s == 'm':
            loop = False
            print(f'Peso Ideal: {((72.7 * h) - 58.0):.2f}')
        elif s == 'F' or s == 'f':
            loop = False
            print(f'Peso Ideal: {((62.1 * h) - 44.7):.2f}')
        else:
            loop = True

except ValueError:
    print('O valor informado esta invalido!')
