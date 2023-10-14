"""
Leia um valor de volume em metros cubicos m3 e apresente-o convertido em litros. A
formula de conversao eh: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cubicos.
"""
try:
    m = float(input('Informe um valor de volume em metros cubicos: '))
    l = 1000 * m
    print(f'L = 1000 * {m}')
    print(f'L = {l}')
except ValueError:
    print('O valor informado esta incorreto!')
