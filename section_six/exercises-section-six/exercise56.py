"""
Faca um programa que calcule a soma de todos os numeros primos abaixo de dois
milhoes
"""


def numero_primo(numero):
    if numero == 1:
        return False

    j = 2
    while j <= numero // 2:
        if numero % j == 0:
            return False
        j = j + 1

    return True


i = 1
soma = 0
while i < 200:
    if numero_primo(i):
        soma = soma + i
    i = i + 1

print(f'SOMA DOS PRIMOS: {soma}')
