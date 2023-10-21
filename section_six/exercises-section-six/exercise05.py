"""
Faca um programa que peca ao usuario para digitar 10 valores e some-os
"""
try:
    contador = 0
    soma = 0
    while contador < 10:
        contador = contador + 1
        numero = float(input(f'Informe o {contador}º numero: '))
        soma = soma + numero

    print(f'SOMA DOS NUMEROS INFORMADOS: {soma}')

except ValueError:
    print('O formato de valor informado esta invalido!')
