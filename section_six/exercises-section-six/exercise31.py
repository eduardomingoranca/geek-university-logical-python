"""
Faca um programa que calcule e escreva o valor de S
            S = 1 + 3 + 5 + 7 + ... + 99
                1   2   3   4 + ...   50
"""
contador = 1
s = 0
while contador <= 50:
    s = s + (2.0 * contador - 1) / contador
    contador = contador + 1

print(f'S: {s:.2f}')
