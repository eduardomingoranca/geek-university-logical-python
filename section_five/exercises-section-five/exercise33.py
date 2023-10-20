"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preco antigo,
calcule e escreva o preco novo, e escreva uma mensagem em funcao do preco novo (de
acordo com a segunda tabela).

            | PRECO ANTIGO               | PERCENTUAL DE AUMENTO |
            | ate R$ 50.00               |          5%           |
            | entre R$ 50.00 e R$ 100.00 |         10%           |
            | acima de R$ 100.00         |         15%           |

            | PRECO NOVO                              | MENSAGEM   |
            | ate R$ 80.00                            |  Barata    |
            | entre R$ 80.00 e R$ 120.00 (inclusive)  |  Normal    |
            | entre R$ 120.00 e R$ 200.00 (inclusive) |   Caro     |
            | acima de R$ 200.00                      | Muito caro |

"""
try:
    preco_antigo = float(input('R$ '))

    if 50.00 > preco_antigo > 200.00:
        if preco_antigo * 1.05 < 80.00:
            print(f'R$ {preco_antigo * 1.05}')
            print('BARATA')
        elif 80.00 <= preco_antigo * 1.05 <= 120.00:
            print(f'R$ {preco_antigo * 1.05}')
            print('NORMAL')
        elif 120.00 < preco_antigo * 1.05 <= 200.00:
            print(f'R$ {preco_antigo * 1.05}')
            print('CARO')
        else:
            print(f'R$ {preco_antigo * 1.05}')
            print('MUITO CARO')

    elif preco_antigo <= 100.00:
        if preco_antigo * 1.10 < 80.00:
            print(f'R$ {preco_antigo * 1.10}')
            print('BARATA')
        elif 80.00 <= preco_antigo * 1.+10 <= 120.00:
            print(f'R$ {preco_antigo * 1.10}')
            print('NORMAL')
        elif 120.00 < preco_antigo * 1.10 <= 200.00:
            print(f'R$ {preco_antigo * 1.10}')
            print('CARO')
        else:
            print(f'R$ {preco_antigo * 1.10}')
            print('MUITO CARO')

    else:
        if preco_antigo * 1.15 < 80.00:
            print(f'R$ {preco_antigo * 1.15}')
            print('BARATA')
        elif 80.00 <= preco_antigo * 1.15 <= 120.00:
            print(f'R$ {preco_antigo * 1.15}')
            print('NORMAL')
        elif 120.00 < preco_antigo * 1.15 <= 200.00:
            print(f'R$ {preco_antigo * 1.15}')
            print('CARO')
        else:
            print(f'R$ {preco_antigo * 1.15}')
            print('MUITO CARO')

except ValueError:
    print('O valor informado esta invalido!')
