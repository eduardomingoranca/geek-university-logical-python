"""
Faca um programa para leia o horario (hora, minuto e segundo) de inicio e a duracao, em
segundos, de uma experiencia biologica. O programa deve resultar com o novo horario
(hora, minuto e segundo) do termino da mesma.
"""
try:
    hora = int(input('Informe um horario (hora, minuto, segundo): '))
    minuto = int(input())
    segundo = int(input())

    duracao = int(input('Informe a duracao em segundos: '))

    print(f'{(duracao // 3600) + hora}:{(duracao % 3600 // 60) + minuto}:{(duracao % 3600 % 60) + segundo}')
except ValueError:
    print('O valor informado esta invalido!')
