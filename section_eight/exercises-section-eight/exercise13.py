"""
Faca uma funcao que receba dois valores numericos e um simbolo. Este simbolo representara
a operacao que se deseja efetuar com os numeros. Se o simbolo for + devera ser realizada
uma adicao, se for - uma subtracao, se for / uma divisao e se for * sera efetuada uma
multiplicacao.
"""


def operacoes_matematicas(v1, v2, s):
    match s:
        case '+':
            return v1 + v2
        case '-':
            return v1 - v2
        case '/':
            return v1 / v2
        case '*':
            return v1 * v2


try:
    loop = True
    while loop:
        n1 = float(input('Informe o 1º numero: '))
        n2 = float(input('Informe o 2º numero: '))
        simbolo = input('Informe o simbolo da operacao matematica (+ - / *): ')

        if simbolo == '+':
            loop = False
            print(f'{n1} + {n2} = {operacoes_matematicas(n1, n2, simbolo)}')
        elif simbolo == '-':
            loop = False
            print(f'{n1} - {n2} = {operacoes_matematicas(n1, n2, simbolo)}')
        elif simbolo == '/':
            loop = False
            print(f'{n1} / {n2} = {operacoes_matematicas(n1, n2, simbolo)}')
        elif simbolo == '*':
            loop = False
            print(f'{n1} * {n2} = {operacoes_matematicas(n1, n2, simbolo)}')

except ValueError:
    print('FORMATO INVALIDO!')
