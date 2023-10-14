"""
Faca um programa que receba um numero inteiro e verifique se este numero eh par ou
impar
"""
try:
    numero = int(input('Informe um numero inteiro: '))

    if numero % 2 == 0:
        print(f'{numero} eh PAR!')
    else:
        print(f'{numero} eh IMPAR!')

except ValueError:
    print('O valor informado esta invalido!')
