"""
Faca um programa que leia um vetor de 10 numeros. Leia um numero x. Conte os
multiplos de um numero inteiro x num vetor e mostre-os na tela.
"""
try:
    loop = True
    contador = 1
    lista = []
    while loop:
        n = float(input(f'Informe o {contador}º numero: '))
        lista.append(n)

        if contador == 10:
            loop = False
            x = int(input('X: '))

            for i in lista:
                if i % x == 0:
                    print(i, end=' ')

        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
