"""
Leia um valor de area em hectares e apresente-o convertido em metros quadrados m2.
A formula de conversao eh: M = H * 1000, sendo M a area em metros quadrados e H
a area em hectares.
"""
try:
    h = float(input('Informe um valor de area em hectares: '))
    m = h * 1000
    print(f'M = {h} * 1000')
    print(f'M = {m}')
except ValueError:
    print('O valor informado esta incorreto!')
