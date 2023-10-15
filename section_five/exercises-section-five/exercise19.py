"""
Faca um programa para verificar se um determinado numero inteiro e divisivel por 3 ou
5, mas nao simultaneamente pelos dois.
"""
try:
    numero = int(input('Informe um numero inteiro: '))

    if numero % 3 == 0:
        print(f'{numero} eh divisivel por 3')
    elif numero % 5 == 0:
        print(f'{numero} eh divisivel por 5')
    else:
        print(f'{numero} nao eh divisivel por 3 ou 5')

except ValueError:
    print('O valor informado esta invalido!')
