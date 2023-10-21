"""
Em Matematica, o numero harmonico designado por H(n) define-se como sendo a soma
da serie harmonica:
                    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faca um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""
try:
    n = int(input('Informe um numero inteiro: '))

    contador = 1
    h = 1
    while contador <= n:
        h = 1 + 1/contador
        contador = contador + 1

    print(f'H({n}) = {h}')

except ValueError:
    print('O formato de valor informado esta invalido!')
