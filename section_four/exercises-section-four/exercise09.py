"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
formula de conversao eh: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin
"""
try:
    celsius = float(input('Informe uma temperatura em graus Celsius: '))
    k = celsius + 273.15
    print(f'K = {celsius} + 273.15')
    print(f'K = {k}')
except ValueError:
    print('O valor informado eh invalido!')
