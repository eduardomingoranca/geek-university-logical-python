"""
Faca uma funcao que retorne o maior fator primo de um numero
"""


def maior_primo(n):
    for num in reversed(range(1, n+1)):
        if all(num % i != 0 for i in range(2, num)):
            return num


try:
    print(maior_primo(10))
except ValueError:
    print('FORMATO INVALIDO!')
