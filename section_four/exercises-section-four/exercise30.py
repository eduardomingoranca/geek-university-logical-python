"""
Leia um valor em real e a cotacao do dolar. Em seguida, imprima o valor correspondente
em dolares.
"""
try:
    real = float(input('R$ '))
    dolar = real / 5.05
    print(f'R$ {real} para $ {dolar:.2f}')
except ValueError:
    print('O valor informado esta incorreto!')
