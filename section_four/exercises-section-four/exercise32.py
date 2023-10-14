"""
Leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de
seu dobro
"""
try:
    numero = int(input('Informe um numero inteiro: '))
    print(f'{(numero+1) * 3 + (numero-1) * 2}')
except ValueError:
    print('O valor informado esta incorreto!')
