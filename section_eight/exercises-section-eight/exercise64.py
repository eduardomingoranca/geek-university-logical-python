"""
Implemente a funcao a qual recebe duas strings, str1 e str2, e concatena a string apontada
por str2 a string apontada por str1.
"""


def concatenacao(st1, st2):
    return st1 + " " + st2


try:
    str1 = input('Informe uma palavra: ')
    str2 = input('Informe outra palavra: ')

    print(f'{concatenacao(str1, str2)}')
except ValueError:
    print('FORMATO INVALIDO!')
