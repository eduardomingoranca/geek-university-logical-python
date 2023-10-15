"""
Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto eh, domingo se 1, segunda-feira se 2, e
assim por diante.
"""
try:
    loop = True
    while loop:
        numero_dia_semana = int(input('Informe um numero inteiro correspondente ao dia da semana (entre 1 e 7): '))

        if numero_dia_semana == 1:
            print('DOMINGO')
        elif numero_dia_semana == 2:
            print('SEGUNDA-FEIRA')
        elif numero_dia_semana == 3:
            print('TERCEIRA-FEIRA')
        elif numero_dia_semana == 4:
            print('QUARTA-FEIRA')
        elif numero_dia_semana == 5:
            print('QUINTA-FEIRA')
        elif numero_dia_semana == 6:
            print('SEXTA-FEIRA')
        elif numero_dia_semana == 7:
            print('SABADO')
        else:
            loop = False
            print('NUMERO INVALIDO!')

except ValueError:
    print('O valor informado esta invalido!')
