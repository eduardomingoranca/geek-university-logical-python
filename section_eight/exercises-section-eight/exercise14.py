"""
Faca uma funcao que receba a distancia em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a tabela abaixo:
                        | CONSUMO   | (Km/l) | MENSAGEM         |
                        | menor que |   8    | Venda o carro!   |
                        | entre     | 8 e 14 | Economico!       |
                        | maior que |   12   | Super economico! |
"""


def consumo_litros(km, lt):
    return km / lt


try:
    quilometros = float(input('Informe o quilometro: '))
    litros = float(input('Informe os listros: '))

    if consumo_litros(quilometros, litros) < 8:
        print('Venda o carro!')
    elif consumo_litros(quilometros, litros) < 14:
        print('Economico!')
    else:
        print('Super economico!')

except ValueError:
    print('FORMATO INVALIDO!')
