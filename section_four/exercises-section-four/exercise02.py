"""
Faca um programa que leia um numero real e o imprima.
"""
try:
    numero = float(input('Informe um numero real: '))
    print(f'O numero informado eh {numero}')
except ValueError:
    print('O valor informado esta invalido!')
