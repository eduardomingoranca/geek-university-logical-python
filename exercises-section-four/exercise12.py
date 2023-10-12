"""
Leia uma distancia em milhas e apresente-a convertida em quilometros. A formula de
conversao eh: K = 1.61 * M, sendo K a distancia em quilometros e M em milhas.
"""
try:
    m = float(input('Informe uma distancia em milhas: '))
    k = 1.61 * m
    print(f'K = 1.61 * {m}')
    print(f'K = {k}')
except ValueError:
    print('O valor informado esta invalido!')
