"""
Faca uma funcao que receba duas strings e retorne a intercalacao letra a letra da primeira
com a segunda string. A string intercalada deve ser retornada na primeira string.
"""


def intercalacao(p1, p2):
    return p1 + " " + p2


try:
    palavra1 = input('Informe uma palavra: ')
    palavra2 = input('Informe outra palavra: ')

    print(f'{intercalacao(palavra1, palavra2)}')
except ValueError:
    print('FORMATO INVALIDO!')
