"""
Faca um programa que leia um numero inteiro positivo N e imprima todos os numeros
naturais de 0 ate N em ordem decrescente.
"""
try:
    n = int(input('Informe o numero: '))

    contador = 0
    while contador <= n:
        print(n)
        n = n - 1

except ValueError:
    print('O formato de valor informado esta invalido!')
