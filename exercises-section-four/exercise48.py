"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""
try:
    segundos = int(input('Informe os segundos: '))

    print(f'{segundos} segundos')

    print(f'{segundos // 3600}:{segundos % 3600 // 60}:{segundos % 3600 % 60}')
except ValueError:
    print('O valor informado esta invalido!')
