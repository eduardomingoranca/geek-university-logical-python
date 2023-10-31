"""
Faca um programa que calcule o desvio padrao de um vetor v contendo n = 10 numeros,
onde m eh a media do vetor.
                            Desvio Padrao = √ 1    Σn  (v[i] - m)²
                                             n-1  i=1
"""
import math

try:
    loop = True
    n = 10
    v = []
    contador = 1
    soma = 0
    while loop:
        v.append(float(input('V: ')))

        if contador == n:
            loop = False
            for i in v:
                soma = soma + i

            m = soma / n

            a = 0.0
            for j in v:
                a = a + pow(j - m, 2.0)

            m2 = a / n

            dp = math.sqrt(m2)

            print(f'Desvio Padrao: {dp:.2f}')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
