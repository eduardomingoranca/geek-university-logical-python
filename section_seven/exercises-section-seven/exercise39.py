"""
Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n
linhas do chamado Triangulo de Pascal:

    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    ...
"""
try:

    def factorial(interador):
        if interador == 0:
            return 1
        return interador * factorial(interador - 1)

    loop = True
    vet = []
    while loop:
        n = int(input('Informe um numero inteiro positivo: '))

        if n > 0:
            loop = False
            i = 0
            while i <= n:
                j = 0
                while j <= i:
                    print(f'{factorial(i)// (factorial(i -j) * factorial(j))}', end=' ')
                    j = j + 1
                print('')
                i = i + 1
except ValueError:
    print('FORMATO INVALIDO!')
