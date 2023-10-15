"""
Calcule as raizes da equacao de 2º grau:
    Lembrando que:
    x = -b +- \/ delta
            2a
          Onde
    delta = B² - 4ac
E ax² + bx + c = 0 representa uma equacao de 2º grau.
A variavel a tem que ser diferente de zero. Caso seja igual, imprima a mensagem 'Nao
eh equacao de segundo grau'.
    <> Se delta < 0, nao existe real. Imprima a mensagem Nao existe raiz.
    <> Se delta == 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz unica.
    <> Se delta >= 0, imprima as duas raizes reais.
"""
import math

try:
    b = float(input('B: '))
    a = float(input('A: '))
    c = float(input('C: '))

    if a == 0:
        print('NAO EH EQUACAO DE SEGUNDO GRAU!')
    else:
        delta = pow(b, 2.0) - 4.0 * a * c

        if delta < 0.0:
            print('NAO EXISTE RAIZ!')
        elif delta == 0.0:
            x1 = -b + math.sqrt(delta) / 2.0 * a * c
            print('RAIZ UNICA!')
            print(f'X1: {x1:.2f}')
        else:
            x1 = -b + math.sqrt(delta) / 2.0 * a * c
            x2 = -b - math.sqrt(delta) / 2.0 * a * c
            print('DUAS RAIZES!')
            print(f'X1: {x1:.2f}')
            print(f'X2: {x2:.2f}')

except ValueError:
    print('O valor informado esta invalido!')
