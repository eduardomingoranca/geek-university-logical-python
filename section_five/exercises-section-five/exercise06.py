"""
Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles,
assim como a diferenca existente entre ambos.
"""
try:
    loop = True
    while loop:
        primeiro_numero = int(input('Informe o 1º numero inteiro: '))
        segundo_numero = int(input('Informe o 2º numero inteiro: '))

        if primeiro_numero == segundo_numero:
            loop = True
        elif primeiro_numero > segundo_numero:
            loop = False
            print(f'{primeiro_numero} > {segundo_numero}')
            print(f'{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero}')
        else:
            loop = False
            print(f'{segundo_numero} > {primeiro_numero}')
            print(f'{segundo_numero} - {primeiro_numero} = {segundo_numero - primeiro_numero}')

except ValueError:
    print('O valor informado esta invalido!')
