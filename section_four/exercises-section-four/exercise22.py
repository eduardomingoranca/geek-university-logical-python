"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros. A formula
de conversao eh: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento
em metros.
"""
try:
    j = float(input('Informe um valor de comprimento em jardas: '))
    m = 0.91 * j
    print(f'M = 0.91 * {j}')
    print(f'M = {m}')
except ValueError:
    print('O valor informado esta incorreto!')
