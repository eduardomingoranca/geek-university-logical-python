"""
Faca uma funcao para verificar se um numero eh positivo ou negativo. Sendo que o valor
de retorno sera 1 se positivo, -1 se negativo e 0 se for igual a 0.
"""


def positivo_negativo(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


try:
    numero = float(input('Informe um numero: '))

    if positivo_negativo(numero) == 1:
        print('NUMERO POSITIVO!')
    elif positivo_negativo(numero) == -1:
        print('NUMERO NEGATIVO!')
    elif positivo_negativo(numero) == 0:
        print('ZERO!')

except ValueError:
    print('FORMATO INVALIDO!')
