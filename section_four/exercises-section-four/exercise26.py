"""
Leia um valor de area em metros quadrados m2 e apresente-o convertido em hectares.
A formula de conversao eh: H = M * 0.0001, sendo M a area em metros quadrados e H
a area em hectares.
"""
try:
    m = float(input('Informe um valor de area em metros quadrados: '))
    h = m * 0.0001
    print(f'H = {m} * 0.0001')
    print(f'H = {h}')
except ValueError:
    print('O valor informado esta incorreto!')