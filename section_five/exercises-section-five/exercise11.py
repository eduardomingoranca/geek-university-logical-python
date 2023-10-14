"""
Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao numero 251 correspondera o valor
8 (2 + 5 + 1). Se o numero lido nao for maior do que zero, o programa terminara com a
mensagem 'Numero invalido'
"""
try:
    numero = int(input('Informe um numero inteiro (0 a 999): '))

    if 0 < numero < 999:
        print(f'{numero} | ({numero // 100} + {numero % 100 // 10} + {numero % 100 % 10})'
              f' {(numero // 100) + (numero % 100 // 10) + (numero % 100 % 10)}')
    else:
        print('Numero invalido!')

except ValueError:
    print('O valor informado esta invalido!')
