"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilometros por hora). A formula de conversao eh: K = M * 3.6, sendo K a velocidade
em km/h e M em m/s.
"""
try:
    m = float(input('Infome uma velocidade em m/s (metros por segundo): '))
    k = m * 3.6
    print(f'K = {m} * 3.6')
    print(f'K = {k}')
except ValueError:
    print('O valor informado esta invalido!')
