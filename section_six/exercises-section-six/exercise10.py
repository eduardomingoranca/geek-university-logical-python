"""
Faca um programa que calcule e mostre a soma dos 50 primeiros numeros pares.
"""
contador = 0
while contador < 50:
    contador = contador + 1
    if contador % 2 == 0:
        print(contador)
    