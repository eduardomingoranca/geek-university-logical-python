"""
Gere matriz 4 x 4 com valores no intervalo[1, 20]. Escreva um programa que transforme
a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos
acima da diagonal principal. Imprima a matriz original e a matriz transformada.
"""
import random

matriz = [[0 for i in range(4)] for j in range(4)]

for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = random.randint(1, 20)

for linha in range(4):
    for coluna in range(4):
        if linha < coluna:
            matriz[linha][coluna] = 0

for linha in range(4):
    for coluna in range(4):
        print(f'{matriz[coluna][linha]}', end=' ')
    print()
