"""
Faca um programa que receba dois numeros e mostre qual deles eh o maior.
"""
try:
    primeiro_numero = int(input('Informe o 1º numero: '))
    segundo_numero = int(input('Informe o 2º numero: '))

    if primeiro_numero > segundo_numero:
        print(f'{primeiro_numero} | {segundo_numero}')
    else:
        print(f'{segundo_numero} | {primeiro_numero}')
except ValueError:
    print('O valor informado esta invalido!')
