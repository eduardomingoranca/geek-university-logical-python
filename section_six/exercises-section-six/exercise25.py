"""
Faca um programa que some todos os numeros naturais abaixo de 1000 que sao multiplos
de 3 ou 5.
"""
contador = 0
soma = 0
while contador < 1000:
    if contador % 3 == 0 or contador % 5 == 0:
        soma = soma + contador
    contador = contador + 1

print(f'SOMA: {soma}')
