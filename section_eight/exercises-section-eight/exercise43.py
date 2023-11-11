"""
Faca uma funcao que receba um vetor de inteiros e o preencha com numeros aleatorios
sem repeticao.
"""
import random


def aleatorios(v):
    for j in v:
        print(j, end=' ')


i = 1
vet = []
s = {}
while i <= 100:
    n = random.randint(i, 100)
    vet.append(n)
    s = set(vet)
    i = i + 1

aleatorios(s)
