"""
O custo ao consumidor de um carro novo eh a soma do custo de fabrica, da comissao
do distribuidor, e dos impostos. A comissao e os impostos sao calculados sobre o
custo de fabrica, de acordo com a tabela abaixo. Leia o custo de fabrica e escreva
o custo ao consumidor.

    | CUSTO DE FABRICA                  | % DO DISTRIBUIDOR | % DOS IMPOSTOS |
    | ate R$ 12.000.00                  |         5         |     isento     |
    | entre R$ 12.000.00 e R$ 25.000.00 |        10         |       15       |
    | acima de R$ 25.000.00             |        15         |       20       |

"""
try:
    custo_fabrica = float(input('Informe o custo de fabrica - R$ '))

    if custo_fabrica <= 12000.00:
        print(f'Custo do Consumidor - R$ {custo_fabrica + (custo_fabrica * 0.05)}')
    elif 12000.00 <= custo_fabrica <= 25000.00:
        print(f'Custo do Consumidor - R$ {custo_fabrica + (custo_fabrica * 0.10) + (custo_fabrica * 0.15)}')
    else:
        print(f'Custo do Consumidor - R$ {custo_fabrica + (custo_fabrica * 0.20) + (custo_fabrica * 0.20)}')

except ValueError:
    print('O formado do dado informado esta invalido!')
