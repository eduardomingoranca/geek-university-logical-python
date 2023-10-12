"""
Leia um numero real e imprima o resultado do quadrado desse numero.
"""
try:
    numero = float(input('Informe um numero real: '))
    quadrado = pow(numero, 2)
    print(f'O numero {numero} ao quadrado eh {quadrado}')
except ValueError:
    print('O valor informado eh invalido!')
