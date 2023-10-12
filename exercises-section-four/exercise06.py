"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversao eh: F = C * (9.0 / 5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""
try:
    celsius = float(input('Informa uma temperatura em graus Celsius: '))
    fahrenheit = celsius * (9.0 / 5.0) + 32.0
    print(f'F = {celsius} * (9.0 / 5.0) + 32.0')
    print(f'F = {fahrenheit}')
except ValueError:
    print('O valor informado eh invalido!')
