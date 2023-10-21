"""
Faca um programa que leia um numero inteiro positivo impar N e imprima todos os
numeros impares de 1 ate N em ordem decrescente.
"""
try:
    loop = True

    while loop:
        n = int(input('Informe um numero impar: '))

        if n % 2 != 0:
            loop = False
            contador = 1
            while contador <= n:
                if n % 2 != 0:
                    print(n)
                n = n - 1

except ValueError:
    print('O formato de valor informado esta invalido!')
