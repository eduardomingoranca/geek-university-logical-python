"""
Leia a distancia em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela
abaixo:
        | CONSUMO   | (Km/l) | MENSAGEM         |
        | menor que |   8    | Venda o carro!   |
        | entre     | 8 e 14 | Economica!       |
        | maior que |  12    | Super economico! |
"""
try:
    km = float(input('Informe a distancia (em Km): '))
    l = float(input('Informe a quantidade de litros de gasolina: '))

    consumo = km / l
    if 8.0 <= consumo <= 14:
        print('ECONOMICA!')
    elif consumo > 12:
        print('SUPER ECONOMICO!')
    else:
        print('VENDA O CARRO!')

except ValueError:
    print('O valor informado esta invalido!')
