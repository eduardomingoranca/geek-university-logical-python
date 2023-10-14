"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
formula de conversa eh: C = K - 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""
try:
    kelvin = float(input('Informe uma temperatura em graus Kelvin: '))
    c = kelvin - 273.15
    print(f'C = {kelvin} - 273.15')
    print(f'C = {c}')
except ValueError:
    print('O valor informado eh invalido!')
