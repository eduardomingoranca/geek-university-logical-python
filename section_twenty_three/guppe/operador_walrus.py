"""
O operador Walrus permite fazer a atribuicao e retorno de valor em uma unica expressao.

variavel := expressao
"""
# nome = 'Geek University'
# print(nome)
#
# print(nome := 'Geek University')

# Python 3.7
# cesta = []
# fruta = input('Informe a fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Informe a fruta: ')
#

# Python 3.8
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)
