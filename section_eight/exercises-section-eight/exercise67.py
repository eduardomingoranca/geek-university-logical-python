"""
Faca uma rotina que receba como parametro um vetor de caracteres e seu tamanho.
A funcao devera de ler uma string do teclado, caractere por caractere.
"""


def get_char(word):
    for i in word:
        print(f'{i}')


try:
    palavra = input('Informe uma palavra: ')

    get_char(palavra)
except ValueError:
    print('FORMATO INVALIDO!')
