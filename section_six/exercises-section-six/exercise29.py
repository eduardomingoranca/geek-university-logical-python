"""
Escreva um programa para calcular o valor da serie, para 5 termos.
            S = 0 + 1/2! + 2/4! + 3/6! + ...
"""


def fatorial_for(numero):
    resultado = 1
    for k in range(1, numero + 1):
        resultado = resultado * k
    return resultado


s = 0
for i in range(0, 5 + 1):
    s = s + i / fatorial_for(i * 2)

print(f'S = {s:.2f}')
