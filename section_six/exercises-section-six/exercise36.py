"""
Faca um programa que calcule a diferenca entre a soma dos quadrados dos primeiros
100 numeros naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros
numeros naturais eh,
                        1² + 2² + ... + 10² = 385
O quadrado da soma dos dez primeiros numeros naturais eh,
                        (1 + 2 + ... + 10)² = 552 = 3025
A diferenca entre a soma dos quadrados dos dez primeiros numeros naturais e o quadrado
da soma eh 3025 - 385 = 2640.
"""
contador = 1
soma_quadrados = 0
quadrado_soma = 0
while contador <= 100:
    soma_quadrados = soma_quadrados + pow(contador, 2.0)
    quadrado_soma = quadrado_soma + contador
    contador = contador + 1

diferenca = pow(quadrado_soma, 2.0) - soma_quadrados
print(f'{pow(quadrado_soma, 2.0)} - {soma_quadrados} = {diferenca}')
