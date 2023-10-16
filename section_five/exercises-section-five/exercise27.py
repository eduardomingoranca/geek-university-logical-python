"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:
                        | Categoria  |        Idade       |
                        | Infantil A |        5 a 7       |
                        | Infantil B |        8 a 10      |
                        | Juvenil A  |       11 a 13      |
                        | Juvenil B  |       14 a 17      |
                        | Senior     | maiores de 18 anos |
"""
try:
    loop = True
    while loop:
        idade = int(input('Informe a idade do nadador: '))

        if 5 <= idade <= 7:
            print('INFANTIL A')
        elif 8 <= idade <= 10:
            print('INFANTIL B')
        elif 11 <= idade <= 13:
            print('JUVENIL A')
        elif 14 <= idade <= 17:
            print('JUVENIL B')
        elif idade >= 18:
            print('SENIOR')
        else:
            loop = False
            print('IDADE FORA DE CATEGORIA!')

except ValueError:
    print('O valor informado esta invalido!')
