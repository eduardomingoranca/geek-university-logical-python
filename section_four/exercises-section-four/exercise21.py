"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas. A formula
de conversao eh: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""
try:
    l = float(input('Informe um valor de massa em libras: '))
    k = l * 0.45
    print(f'K = {l} * 0.45')
    print(f'K = {k}')
except ValueError:
    print('O valor informado esta incorreto!')
