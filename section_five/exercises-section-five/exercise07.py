"""
Faca um programa que receba dois numeros e mostre o maior. Se por acaso, os dois
numeros forem iguais, imprima a mensagem Numeros iguais.
"""
try:
    primeiro_numero = int(input('Informe o 1º numero inteiro: '))
    segundo_numero = int(input('Informe o 2º numero inteiro: '))

    if primeiro_numero == segundo_numero:
        print('Numeros iguais')
    elif primeiro_numero > segundo_numero:
        print(f'{primeiro_numero}')
    else:
        print(f'{segundo_numero}')

except ValueError:
    print('O valor informado esta invalido!')
