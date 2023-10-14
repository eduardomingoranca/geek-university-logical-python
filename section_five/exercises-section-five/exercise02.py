"""
Leia um numero fornecido pelo usuario. Se esse numero for positivo, calcule a raiz
quadrada do numero. Se o numero for negativo, mostre uma mensagem dizendo que o
numero eh invalido.
"""
import math

try:
    numero = float(input('Informe um numero: '))

    if numero > 0:
        print(f'\/{numero} = {math.sqrt(numero):.2f}')
    else:
        print('!informe apenas numero positivo!')

except ValueError:
    print('O valor informado esta invalido!')
