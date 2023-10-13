"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras. A formula
de conversao eh: L = K/0.45, sendo K a massa em quilogramas e L a massa em libras.
"""
try:
    k = float(input('Informe um valor de massa em quilogramas: '))
    l = k / 0.45
    print(f'L = {k} / 0.45')
    print(f'L = {l:.2f}')
except ValueError:
    print('O valor informado esta incorreto!')
