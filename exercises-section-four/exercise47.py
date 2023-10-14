"""
Leia um numero inteiro de 4 digitos (de 1000 e 9999) e imprima 1 digito por linha.
"""
try:
    numero = int(input('Informe um numero (de 1000 e 9999): '))

    while numero < 1000 or numero > 9999:
        numero = int(input('Informe um numero (de 1000 e 9999): '))

    a = numero // 1000
    b = numero % 1000 // 100
    c = numero % 1000 % 100 // 10
    d = numero % 1000 % 100 % 10

    print(f'{a}')
    print(f'{b}')
    print(f'{c}')
    print(f'{d}')
except ValueError:
    print('O valor informado esta incorreto!')
