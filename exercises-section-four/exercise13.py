"""
Leia uma distancia em quilometros e apresente-a convertida em milhas. A formula de
conversao eh: M = K/1.61, sendo K a distancia em quilometros e M em milhas.
"""
try:
    k = float(input('Informe uma distancia em quilometros: '))
    m = k/1.61
    print(f'M = {k} / 1.61')
    print(f'M = {m:.2f}')
except ValueError:
    print('O valor informado esta invalido!')