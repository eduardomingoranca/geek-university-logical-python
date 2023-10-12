"""
Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s
(metros por segundo). A formula de conversao eh: M = K/3.6, sendo K a velocidade em
km/h e M em m/s.
"""
try:
    k = float(input('Informe uma velocidade em km/h (quilometros por hora): '))
    m = k / 3.6
    print(f'M = {k} / 3.6')
    print(f'M = {m:.2f}')
except ValueError:
    print('O valor informado eh invalido!')
