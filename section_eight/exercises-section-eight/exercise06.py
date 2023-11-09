"""
Faca uma funcao que receba 3 numeros inteiros como parametro, representando horas,
minutos e segundos, e os converta em segundos.
"""


def converte_segundos(h, m, s):
    return h * 3600 + m * 60 + s


try:
    horas = int(input('horas: '))
    minutos = int(input('minutos: '))
    segundos = int(input('segundos: '))

    print(f'{converte_segundos(horas, minutos, segundos)} segundos')
except ValueError:
    print('FORMATO INVALIDO!')
