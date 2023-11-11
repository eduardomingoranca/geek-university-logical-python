"""
Crie uma funcao que receba como parametro um valor inteiro e gere como saida n linhas
com pontos de exclamacao, conforme o exemplo abaixo (para n = 5):
    !
    !!
    !!!
    !!!!
    !!!!!
"""


def floyd(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print('!', end=' ')
            j = j + 1
        print()
        i = i + 1


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro: '))

        if numero > 0:
            loop = False
            floyd(numero)

except ValueError:
    print('FORMATO INVALIDO!')
