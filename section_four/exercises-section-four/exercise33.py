"""
Leia o tamanho do lado de um quadrado e imprima como resultado a sua area.
"""
try:
    lado = float(input('informe o tamanho do lado de um quadrado: '))
    area = pow(lado, 2)
    print(f'A = {lado}²')
    print(f'A = {area}')
except ValueError:
    print('O valor informado esta incorreto!')
