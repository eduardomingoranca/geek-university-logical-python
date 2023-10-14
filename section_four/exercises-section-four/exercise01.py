"""
Faca um programa que leia um numero inteiro e o imprima.
"""
try:
    numero = int(input('Informe um numero inteiro: '))
    print(f'O numero informado eh {numero}')
except ValueError:
    print('O valor informado esta invalido')
