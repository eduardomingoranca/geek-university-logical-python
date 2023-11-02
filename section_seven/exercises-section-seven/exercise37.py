"""
Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 >
... > A11, ou seja, esta ordenado em ordem crescente ate o sexto elemento, e a partir
desse elemento esta ordenado em ordem decrescente. Dado o vetor da questao anterior,
proponha um algoritmo para ordenar os elementos.
"""

vet = [1, 2, 3, 4, 5, 20, 19, 18, 17, 16, 15]
vet.sort()

for i in vet:
    print(i, end=' ')
