"""
Faca um programa que some os numeros primos existentes entre a e b, onde a e b sao
numeros informados pelo usuario.
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
        a = int(input('A: '))
        b = int(input('B: '))

        soma = 0
        if a > b:
            loop = False
            while b <= a:
                if numero_primo(b):
                    soma = soma + b
                b = b + 1

            print(f'SOMA DOS PRIMOS: {soma}')
        elif b > a:
            loop = False
            while a <= b:
                if numero_primo(a):
                    soma = soma + a
                a = a + 1

            print(f'SOMA DOS PRIMOS: {soma}')

except ValueError:
    print('O formato de valor informado esta invalido!')
