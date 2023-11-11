"""
Faca uma funcao 'Troque', que recebe duas variaveis reais A e B e troca o valor delas
(i.e., A recebe o valor de B e B recebe o valor de A).
"""


def troque(a, b):
    aux = a
    a = b
    b = aux

    return f'{a} | {b}'


try:
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))

    print(f'{n1} | {n2} \n{troque(n1, n2)}')
except ValueError:
    print('FORMATO INVALIDO!')
