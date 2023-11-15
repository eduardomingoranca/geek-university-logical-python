"""
Implemente a funcao a qual recebe duas strings, str1 e str2, e um valor inteiro positivo
N. A funcao concatena nao mais que N caracteres da string apontada por str2 a string apontada
por str1 e termina str1 com NULL.
"""
import math


def concatenacao_strings(st1, st2, numero):
    p = st1 + " " + st2
    return p[:numero]


try:
    str1 = input('Informe uma palavra: ')
    str2 = input('Informe outra palavra: ')
    n = int(input('Informe a quantidade de caracteres: '))

    print(concatenacao_strings(str1, str2, n))
except ValueError:
    print('FORMATO INVALIDO!')
