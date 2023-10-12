"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A formula de conversao eh: C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.
"""
try:
    fahrenheit = float(input('Informe uma temperatura em graus Fahrenheit: '))
    c = 5.0 * (fahrenheit - 32.0) / 9.0
    print(f'C = 5.0 * ({fahrenheit} - 32.0) / 9.0')
    print(f'C = {c}')
except ValueError:
    print('O valor informado eh invalido!')
