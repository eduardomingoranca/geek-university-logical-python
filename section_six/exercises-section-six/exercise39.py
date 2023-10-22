"""
Faca um programa que calcule a area de um triangulo, cuja base e altura sao fornecidas
pelo usuario. Esse programa nao pode permitir a entrada de dados invalidos, ou seja,
medidas menores ou iguais a 0.
"""
try:
    loop = True
    while loop:
        b = float(input('base do triangulo: '))
        h = float(input('altura do triangulo: '))

        if b > 0 or h > 0:
            loop = False
            print(f'AREA DO TRIANGULO: {(b * h) / 2.0}')

except ValueError:
    print('O formato de valor informado esta invalido!')
