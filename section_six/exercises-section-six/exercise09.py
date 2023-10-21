"""
Faca um programa que leia um numero inteiro N e depois imprima os N primeiros
numeros naturais impares
"""
try:
    n = int(input('Informe o numero: '))

    contador = 0
    while contador <= n:
        if contador % 2 != 0:
            print(contador)
        contador = contador + 1

except ValueError:
    print('O formato de valor informado esta invalido!')
