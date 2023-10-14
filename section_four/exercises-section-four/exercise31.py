"""
Leia um numero inteiro e imprima o seu antecessor e o seu sucessor
"""
try:
    numero = int(input('Imforme um numero inteiro: '))
    print(f'{numero - 1} {numero} {numero + 1}')
except ValueError:
    print('O valor informado esta incorreto!')
