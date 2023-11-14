"""
Crie uma funcao que calcula o comprimento de uma string.
"""


def tamanho(p):
    return len(p)


try:
    palavra = input('Informe uma palavra: ')

    print(f'A palavra {palavra} tem o comprimento de {tamanho(palavra)} caracteres.')
except ValueError:
    print('FORMATO INVALIDO!')
