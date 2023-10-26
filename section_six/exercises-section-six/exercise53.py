"""
Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n
linhas do chamado Triangulo de Floyd. Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
try:
    loop = True
    while loop:
        n = int(input('N: '))

        if n > 0:
            loop = False
            number = 1
            i = 1
            while i <= n:
                j = 1
                while j <= i:
                    print(f' {number}', end='')
                    number = number + 1
                    j = j + 1
                print('')
                i = i + 1

except ValueError:
    print('O formato de valor informado esta invalido!')
