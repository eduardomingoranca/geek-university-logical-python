"""
Faca uma funcao que receba uma temperatura em graus Celsius e retorne-a convertida
em graus Fahrenheit. A formula de conversao eh: F = C * (9.0 / 5.0) + 32.0, sendo F a
temperatura em Fahrenheit e C a temperatura em Celsius.
"""


def converte_fahrenheit(c):
    return c * (9.0 / 5.0) + 32.0


try:
    celsius = float(input('Informe a temperatura em graus Celsius: '))

    print(f'F = {celsius} * (9.0 / 5.0) + 32.0')
    print(f'F = {converte_fahrenheit(celsius)}')
except ValueError:
    print('FORMATO INVALIDO!')
