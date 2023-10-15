"""
Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mes
correspondente a este numero. Isto eh, janeiro se 1, feveiro se 2, e
assim por diante.
"""
try:
    loop = True
    while loop:
        numero_mes = int(input('Informe o numero correspondente ao mes (entre 1 e 12): '))

        if numero_mes == 1:
            print('JANEIRO')
        elif numero_mes == 2:
            print('FEVEREIRO')
        elif numero_mes == 3:
            print('MARCO')
        elif numero_mes == 4:
            print('ABRIL')
        elif numero_mes == 5:
            print('MAIO')
        elif numero_mes == 6:
            print('JUNHO')
        elif numero_mes == 7:
            print('JULHO')
        elif numero_mes == 8:
            print('AGOSTO')
        elif numero_mes == 9:
            print('SETEMBRO')
        elif numero_mes == 10:
            print('OUTUBRO')
        elif numero_mes == 11:
            print('NOVEMBRO')
        elif numero_mes == 12:
            print('DEZEMBRO')
        else:
            loop = False
            print('NUMERO INVALIDO!')

except ValueError:
    print('O valor informado esta invalido!')
