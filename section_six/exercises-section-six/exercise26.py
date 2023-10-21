"""
Faca um algoritmo que encontre o primeiro multiplo de 11, 13 ou 17 apos um numero
dado.
"""
try:
    n = int(input('Informe um numero inteiro: '))

    contador = 1
    multiplo = 0
    while contador <= n:
        if contador % 11 == 0 or contador % 13 == 0 or contador % 17 == 0:
            print(f'PRIMEIRO MULTIPLO: {contador}')
            break
        contador = contador + 1

except ValueError:
    print('O formato de valor informado esta invalido!')
