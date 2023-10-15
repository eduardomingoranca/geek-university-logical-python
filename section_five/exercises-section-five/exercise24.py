"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%;
MS 8%). Faca um programa em que o usuario entre com o valor e o estado destino
do produto e o programa retorne o preco final do produto acrescido do imposto
do estado em que ele sera vendido. Se o estado digitado nao for valido, mostrar
uma mensagem de erro.
"""
try:
    loop = True
    while loop:
        valor_produto = float(input('Informe o valor do produto - R$ '))

        print('=======================')
        print('| [1] - MG | [2] - SP |')
        print('| [3] - RJ | [4] - MS |')
        print('=======================')

        opcao = int(input('Informe o estado que o produto sera vendido: '))

        if opcao == 1:
            print('===== MINAS GERAIS =====')
            print(f'IMPOSTO DE 7% - R$ {valor_produto * 0.07} '
                  f'| PRECO DO PRODUTO - R$ {valor_produto + (valor_produto * 0.07)}')
        elif opcao == 2:
            print('===== SAO PAULO =====')
            print(f'IMPOSTO DE 12% - R$ {valor_produto * 0.12} '
                  f'| PRECO DO PRODUTO - R$ {valor_produto + (valor_produto * 0.12)}')
        elif opcao == 3:
            print('===== RIO DE JANEIRO =====')
            print(f'IMPOSTO DE 15% - R$ {valor_produto * 0.15} '
                  f'| PRECO DO PRODUTO - R$ {valor_produto + (valor_produto * 0.15)}')
        elif opcao == 4:
            print('===== MATO GROSSO DO SUL =====')
            print(f'IMPOSTO DE 8% - R$ {valor_produto * 0.08} '
                  f'| PRECO DO PRODUTO - R$ {valor_produto + (valor_produto * 0.08)}')
        else:
            loop = False
            print('ESTADO INVALIDO!')

except ValueError:
    print('O valor informado esta invalido!')
