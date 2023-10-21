"""
Faca um programa que leia um numero inteiro positivo par N e imprima todos os numeros
pares de 0 ate N em ordem crescente.
"""
try:
    loop = True

    while loop:
        n = int(input('Informe um numero par: '))

        if n % 2 == 0:
            loop = False
            contador = 0
            while contador <= n:
                if contador % 2 == 0:
                    print(contador)
                contador = contador + 1

except ValueError:
    print('O formato de valor informado esta invalido!')
