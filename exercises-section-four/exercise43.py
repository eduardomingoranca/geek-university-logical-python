"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
        . o total a pagar com desconto de 10%;
        . o valor de cada parcela, no parcelamento de 3x sem juros;
        . a comissao do vendedor, no caso da venda ser a vista (5% sobre o valor com
        desconto)
        . a comissao do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
try:
    valor_total = float(input('Informe o valor total do produto - R$ '))

    total_pagar_desconto = valor_total - valor_total * 0.10
    print(f'o total a pagar com desconto de 10% - R$ {total_pagar_desconto}')

    print(f'o valor de cada parcela, no parcelamento de 3x sem juros - R$ {(valor_total / 3.0):.2f}')

    comissao_vendedor_a_vista = total_pagar_desconto - (total_pagar_desconto * 0.05)
    print(f'a comissao do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto) - '
          f'R$ {comissao_vendedor_a_vista}')

    comissao_vendedor_venda_parcelada = valor_total - (valor_total * 0.05)
    print(f'a comissao do vendedor, no caso da venda ser parcelada (5% sobre o valor total) - '
          f'R$ {comissao_vendedor_venda_parcelada}')
except ValueError:
    print('O valor informado esta incorreto!')
