"""
Faca uma funcao que calcule o desvio padrao de um vetor v contendo n numeros
desvio padrao: √  1    Σⁿ i = 1 (v[i] - m)²
                n - 1
onde m eh a media do vetor
"""
import math


def desvio_padrao(vet, a):
    soma = 0
    for j in vet:
        soma = soma + j

    m = soma / a

    s = 0
    for p in vet:
        s = s + pow(p - m, 2.0)

    dp = math.sqrt(s / a)

    return dp


try:
    loop = True
    i = 1
    v = []
    while loop:
        n = float(input(f'Informe o {i}º numero positivo: '))

        if n < 0:
            loop = False
            print(f'DP: {desvio_padrao(v, i-1):.4f}')

        v.append(n)
        i = i + 1
except ValueError:
    print('FORMATO INVALIDO!')
