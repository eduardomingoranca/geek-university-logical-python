"""
Faca um programa que leia um numero inteiro positivo n e calcule a soma dos n primeiros
numeros naturais.
"""
try:
    loop = True

    while loop:
        n = int(input('Informe um numero inteiro positivo: '))

        if n > 0:
            loop = False
            contador = 0
            soma = 0
            while contador <= n:
                soma = soma + contador
                contador = contador + 1

            print(f'SOMA: {soma}')

except ValueError:
    print('O formato de valor informado esta invalido!')
