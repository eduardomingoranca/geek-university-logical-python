"""
Faca um programa que gera um numero aleatorio de 1 a 1000. O usuario deve tentar
acertar qual o numero foi gerado, a cada tentativa o programa devera informar se o
chute eh menor ou maior que o numero gerado. O programa acaba quando o usuario
acertar o numero gerado. O programa deve informar em quantas tentativas o numero foi
descoberto.
"""
from random import randint

try:
    total_tentativas = 0
    loop = True
    while loop:
        numero = int(input('Qual eh o numero? '))

        numero_aleatorio = randint(1, 1000)

        if numero > numero_aleatorio:
            print(f'O numero eh menor que {numero}')
            total_tentativas = total_tentativas + 1
        elif numero < numero_aleatorio:
            print(f'O numero eh maior que {numero}')
            total_tentativas = total_tentativas + 1
        else:
            loop = False
            print(f'O total de tentativas: {total_tentativas}')

except ValueError:
    print('O formato de valor informado esta invalido!')
