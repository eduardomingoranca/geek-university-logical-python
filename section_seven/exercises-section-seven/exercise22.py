"""
Faca um programa que leia dois vetores de 10 posicoes e calcule outro vetor contendo,
nas posicoes pares os valores do primeiro e nas posicoes impares os valores do segundo.
"""
try:
    loop = True
    v1 = []
    v2 = []
    v3 = []
    contador = 1
    i = 0
    j = 0
    while loop:
        v1.append(float(input(f'V1[{contador}]: ')))
        v2.append(float(input(f'V2[{contador}]: ')))

        if contador == 10:
            loop = False
            while i < len(v1):
                if i % 2 == 0:
                    v3.append(v1[i])
                i = i + 1

            while j < len(v2):
                if j % 2 != 0:
                    v3.append(v2[j])
                j = j + 1

            for a in v3:
                print(a, end=' ')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
