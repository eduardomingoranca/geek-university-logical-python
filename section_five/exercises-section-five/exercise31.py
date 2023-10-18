"""
Faca um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostra qual a classificacao dessa pessoa.

        |       Altura   |                  Peso                            |
        |                | Ate 60 | Entre 60 e 90 (Inclusive) | Acima de 90 |
        | Menor que 1.20 |   A    |           D               |      G      |
        | De 1.20 a 1.70 |   B    |           E               |      H      |
        | Maior que 1.70 |   C    |           F               |      I      |

"""
try:
    altura = float(input('Informe a altura: '))
    peso = float(input('Informe o peso: '))

    if altura < 1.20:
        if peso < 60:
            print('A')
        elif 60 <= peso <= 90:
            print('D')
        else:
            print('G')
    elif 1.20 <= altura <= 1.70:
        if peso < 60:
            print('B')
        elif 60 <= peso <= 90:
            print('E')
        else:
            print('H')
    else:
        if peso < 60:
            print('C')
        elif 60 <= peso <= 90:
            print('F')
        else:
            print('I')

except ValueError:
    print('O valor informado esta invalido!')
