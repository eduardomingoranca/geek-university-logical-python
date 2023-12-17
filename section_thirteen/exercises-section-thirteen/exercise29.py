"""
Codifique um programa que manipule um arquivo contendo registros descritos pelos seguintes
campos: codigo_vendedor, nome_vendedor, valor_da_venda e mes.
"""

with open('files/seller_registration.txt', 'w') as file:
    while True:
        codigo_vendedor = int(input('Informe o codigo de vendedor: '))
        nome_vendedor = input('Informe o nome de vendedor: ')
        valor_da_venda = float(input('Informe o valor do venda: '))
        mes = input('Informe o mes: ')

        file.write(str(codigo_vendedor) + ' ' + nome_vendedor + ' ' + str(valor_da_venda)
                   + ' ' + mes)
        file.write('\n')

        opcao = input('Deseja continuar? (s/n) ')
        if opcao == 'n' or opcao == 'N':
            break
