"""
Escrever um programa que leia o codigo do produto escolhido de uma lanchonete
e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execucao somente sera calculado um pedido. O cardapio da
lanchonete segue o padrao abaixo:

            | Especificacao   | Codigo | Preco |
            | Cachorro Quente |  100   | 1.20  |
            | Bauru Simples   |  101   | 1.30  |
            | Bauru com Ovo   |  102   | 1.50  |
            | Hamburguer      |  103   | 1.20  |
            | Chesseburguer   |  104   | 1.70  |
            | Suco            |  105   | 2.20  |
            | Refrigerante    |  106   | 1.00  |

"""
try:
    loop = True
    while loop:
        print('| Especificacao   | Codigo | Preco |')
        print('| Cachorro Quente |  100   | 1.20  |')
        print('| Bauru Simples   |  101   | 1.30  |')
        print('| Bauru com Ovo   |  102   | 1.50  |')
        print('| Hamburguer      |  103   | 1.20  |')
        print('| Cheeseburguer   |  104   | 1.70  |')
        print('| Suco            |  105   | 2.20  |')
        print('| Refrigerante    |  106   | 1.00  |')

        codigo = int(input('Selecione o codigo: '))

        if codigo == 100:
            quantidade = int(input('Informe a quantidade de Cachorro Quente: '))
            valor_final = 1.20 * quantidade
            print(f'PRECO FINAL = R$ {valor_final}')
        elif codigo == 101:
            quantidade = int(input('Informe a quantidade de Bauru Simples: '))
            valor_final = 1.30 * quantidade
            print(f'PRECO FINAL = R$ {valor_final}')
        elif codigo == 102:
            quantidade = int(input('Informe a quantidade de Bauru com Ovo: '))
            valor_final = 1.50 * quantidade
            print(f'PRECO FINAL = R$ {valor_final}')
        elif codigo == 103:
            quantidade = int(input('Informe a quantidade de Hamburguer: '))
            valor_final = 1.20 * quantidade
            print(f'PRECO FINAL = R$ {valor_final}')
        elif codigo == 104:
            quantidade = int(input('Informe a quantidade de Cheeseburguer: '))
            valor_final = 1.70 * quantidade
            print(f'PRECO FINAL = R$ {valor_final}')
        elif codigo == 105:
            quantidade = int(input('Informe a quantidade de Suco: '))
            valor_final = 2.20 * quantidade
            print(f'PRECO FINAL = R$ {valor_final}')
        elif codigo == 106:
            quantidade = int(input('Informe a quantidade de Refrigerante: '))
            valor_final = 1.00 * quantidade
            print(f'PRECO FINAL = R$ {valor_final}')
        else:
            loop = False
            print('CODIGO INVALIDO!')

except ValueError:
    print('O valor informado esta invalido!')
