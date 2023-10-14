"""
Leia um valor de area em metros quadrados m2 e apresente-o convertido em acres. A
formula de conversao eh: A = M * 0.000247, sendo M a area em metros quadrados e A
area em acres.
"""
try:
    m = float(input('Informe um valor de area em metros quadrados: '))
    a = m * 0.000247
    print(f'A = {m} * 0.000247')
    print(f'A = {a}')
except ValueError:
    print('O valor informado esta incorreto!')
