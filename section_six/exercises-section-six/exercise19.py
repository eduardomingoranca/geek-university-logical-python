"""
Escreva um algoritmo que leia um numero inteiro entre 100 e 999 a imprima na saida
cada um dos algarismos que compoem o numero.
"""
try:
    loop = True
    while loop:
        n = int(input('Informe um numero inteiro (entre 100 e 999): '))

        if 100 <= n <= 999:
            loop = False
            print(f'{n // 100}')
            print(f'{n % 100 // 10}')
            print(f'{n % 100 % 10}')

except ValueError:
    print('O formato de valor informado esta invalido!')
