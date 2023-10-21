"""
Faca um programa que determine o mostre os cinco primeiros multiplos de 3, considerando
numeros maiores que 0.
"""
for numero in range(1, 6):
    if numero % 3 == 0 and numero > 0:
        print(numero)
