"""
Faca um programa que leia 10 inteiros e imprima sua media
"""
try:
    contador = 0
    soma = 0
    while contador < 10:
        contador = contador + 1
        numero = int(input(f'Informe o {contador}º numero: '))
        soma = soma + numero

    print(f'A MEDIA DA SOMA DOS NUMEROS: {soma / contador}')

except ValueError:
    print('O formato de valor informado esta invalido!')
