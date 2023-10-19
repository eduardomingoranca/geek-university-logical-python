"""
Escreva um programa que, dado o valor da venda, imprima a comissao que devera ser
paga ao vendedor. Para calcular a comissao, considere a tabela abaixo:

    | Venda mensal                                            | Comissao                   |
    | Maior ou igual a R$ 100.000,00                          | R$ 700.00 + 16% das vendas |
    | Menor que R$ 100.000,00 e maior ou igual a R$ 80.000,00 | R$ 650.00 + 14% das vendas |
    | Menor que R$ 80.000,00 e maior ou igual a R$ 60.000,00  | R$ 600.00 + 14% das vendas |
    | Menor que R$ 60.000,00 e maior ou igual a R$ 40.000,00  | R$ 550.00 + 14% das vendas |
    | Menor que R$ 40.000,00 e maior ou igual a R$ 20.000,00  | R$ 500.00 + 14% das vendas |
    | Menor que R$ 20.000,00                                  | R$ 400.00 + 14% das vendas |

"""
try:
    venda = float(input('VENDA - R$ '))

    if venda >= 100.000:
        print(f'COMISSAO - R$ {(700.00 + venda * 0.16):.2f}')
    elif venda < 100.000:
        print(f'COMISSAO - R$ {(650.00 + venda * 0.14):.2f}')
    elif venda < 80.000:
        print(f'COMISSAO - R$ {(600.00 + venda * 0.14):.2f}')
    elif venda < 60.000:
        print(f'COMISSAO - R$ {(550.00 + venda * 0.14):.2f}')
    elif venda < 40.000:
        print(f'COMISSAO - R$ {(500.00 + venda * 0.14):.2f}')
    elif venda < 20.000:
        print(f'COMISSAO - R$ {(400.00 + venda * 0.14):.2f}')

except ValueError:
    print('O formado do dado informado esta invalido!')

