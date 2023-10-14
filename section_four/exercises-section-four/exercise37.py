"""
Faca um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%
"""
try:
    produto = float(input('Produto - R$ '))
    produto -= (produto * 0.12)
    print(f'R$ {produto} com desconto de 12%')
except ValueError:
    print('O valor informado esta incorreto!')
