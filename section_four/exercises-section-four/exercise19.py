"""
Leia um valor de volume e apresente-o convertido em metros cubicos m3. A
formula de conversao eh: M = L/1000, sendo L o volume em litros e M o volume
em metros cubicos.
"""
try:
    l = float(input('Informe um valor de volume: '))
    m = l / 1000
    print(f'M = {l} / 1000')
    print(f'M = {m}')
except ValueError:
    print('O valor informado esta incorreto!')