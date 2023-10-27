"""
Escreva um programa que leia um inteiro nao negativo n e imprima a soma dos n primeiros
numeros primos.
"""


def numero_primo(numero):
    if numero == 1:
        return False

    j = 2
    while j <= numero // 2:
        if numero % j == 0:
            return False
        j = j + 1

    return True


try:
    loop = True
    while loop:
        n = int(input('Informe um numero inteiro positivo: '))

        if n > 1:
            loop = False
            i = 1
            soma = 0
            while i <= n:
                if numero_primo(i):
                    soma = soma + i
                i = i + 1

            print(f'SOMA DOS PRIMOS: {soma}')

except ValueError:
    print('O formato de valor informado esta invalido!')
