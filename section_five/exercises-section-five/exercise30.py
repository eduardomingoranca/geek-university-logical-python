"""
Faca um programa que receba tres numeros e mostre-os em ordem crescente.
"""
try:
    loop = True
    while loop:
        numero_um = int(input('Informe o 1º numero: '))
        numero_dois = int(input('Informe o 2º numero: '))
        numero_tres = int(input('Informe o 3º numero: '))

        if numero_um > numero_dois > numero_tres:
            print(f'{numero_um} {numero_dois} {numero_tres}')
        elif numero_um > numero_tres > numero_dois:
            print(f'{numero_um} {numero_tres} {numero_dois}')
        elif numero_dois > numero_um > numero_tres:
            print(f'{numero_dois} {numero_um} {numero_tres}')
        elif numero_dois > numero_tres > numero_um:
            print(f'{numero_dois} {numero_tres} {numero_um}')
        elif numero_tres > numero_um > numero_dois:
            print(f'{numero_tres} {numero_um} {numero_dois}')
        elif numero_tres > numero_dois > numero_um:
            print(f'{numero_tres} {numero_dois} {numero_um}')
        else:
            loop = False
            print('NUMEROS IGUAIS!')

except ValueError:
    print('O valor informado esta invalido!')
