"""
Faca uma funcao chamada 'simplifica' que recebe como parametro o numerador e o denominador
de uma funcao. Esta funcao deve simplificar a fracao recebida dividindo o numerador e o
denominador pelo maior fator possivel. Por exemplo, a fracao 36/60 simplifica para 3/5
dividindo o numerador e o denominador por 12. A funcao deve modificar as variaveis passadas
como parametro.
"""


def simplifica(numerador, denominador):
    if numerador < denominador:
        i = numerador
        f1 = 0
        f2 = 0
        while i >= 1:
            if numerador % i == 0 and denominador % i == 0:
                f1 = numerador // i
                f2 = denominador // i
                break
            i = i - 1

        return f'{f1} / {f2}'
    elif denominador < numerador:
        i = denominador
        f1 = 0
        f2 = 0
        while i >= 1:
            if numerador % i == 0 and denominador % i == 0:
                f2 = numerador // i
                f1 = denominador // i
                break
            i = i - 1

        return f'{f2} / {f1}'


try:
    loop = True
    while loop:
        print('Informe o numerador e o denominador da fracao: ')
        n = int(input())
        d = int(input())

        if n > 0 and d > 0:
            loop = False
            print(simplifica(n, d))

except ValueError:
    print('FORMATO INVALIDO!')
