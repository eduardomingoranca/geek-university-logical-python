"""
Faca um programa para gerar automaticamente numeros entre 0 e 99 de uma cartela de
bingo sabendo que cada cartela devera conter 5 linhas de 5 numeros, gere estes dados
de modo a nao ter numeros repetidos dentro das cartelos. O programa deve exibir na
tela a cartela gerada.
"""
import random

cartela = [[0 for i in range(5)] for j in range(5)]
s = {0}

for linha in range(5):
    for coluna in range(5):
        cartela[linha][coluna] = random.randint(0, 99)
        s.add(cartela[linha][coluna])

for i in s:
    print(i, end=' ')
