"""
Uma empresa contrata um encanador a R$ 30.00 por dia. Faca um programa que solicite
o numero de dias trabalhados pelo encanador e imprima a quantia liquida que devera ser
paga, sabendo se que sao descontados 8%  para imposto de renda.
"""
try:
    quantidade_dias = int(input('Informe o numero de dias trabalhados pelo encanador: '))
    pagamento_encanador = (30.00 * quantidade_dias) - ((30.00 * quantidade_dias) * 0.08)
    print(f'O encanador trabalhou por {quantidade_dias} dias e recebera o pagamento de R$ {pagamento_encanador}')
except ValueError:
    print('O valor informado esta incorreto!')
