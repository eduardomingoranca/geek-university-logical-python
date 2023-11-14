"""
Escreva uma funcao que retorne a primeira posicao de uma sub-string dentro de uma
string. Caso a sub-string nao seja encontrada, a funcao deve retornar -1.
"""


def buscar_letra(p, lt):
    n = len(p) - 1
    let = palavra[:-n]

    if lt == let:
        return 0

    return -1


try:
    palavra = input('Informe uma palavra: ')

    loop = True
    while loop:
        letra = input('Informe a primeira letra na palavra: ')

        v = buscar_letra(palavra, letra)

        if v == 0:
            loop = False
            print(f'A letra {letra} eh a primeira letra na palavra {palavra}')

except ValueError:
    print('FORMATO INVALIDO!')
