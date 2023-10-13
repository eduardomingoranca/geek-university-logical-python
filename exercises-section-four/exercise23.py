"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas. A formula
de conversao eh: J = M / 0.91, sendo J o comprimento em jardas e M o comprimento em
metros.
"""
try:
    m = float(input('Informe um valor de comprimento em metros: '))
    j = m / 0.91
    print(f'J = {m} / 0.91')
    print(f'J = {j:.2f}')
except ValueError:
    print('O valor informado esta incorreto!')
