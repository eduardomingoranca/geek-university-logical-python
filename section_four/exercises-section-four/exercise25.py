"""
Leia um valor de area em acres e apresente-o convertido em metros quadrados m2. A
formula de conversao eh: M = A * 4048.58, sendo M a area em metros quadrados e A a
area em acres.
"""
try:
    a = float(input('Informe um valor de area em acres: '))
    m = a * 4048.58
    print(f'M = {a} * 4048.58')
    print(f'M = {m}')
except ValueError:
    print('O valor informado esta incorreto!')