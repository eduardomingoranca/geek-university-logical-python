"""
Faca um programa que leia 10 inteiros positivos, ignorando nao positivos, e imprima sua
media
"""
try:
    contador = 0
    soma = 0
    while contador < 10:
        contador = contador + 1
        numero = int(input(f'Informe o {contador}º numero: '))

        if numero < 0:
            continue

        soma = soma + numero

    print(f'A MEDIA DA SOMA DOS NUMEROS POSITIVOS: {soma / contador}')

except ValueError:
    print('O formato de valor informado esta invalido!')
