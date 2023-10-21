"""
Faca um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E,
conforme a formula a seguir:
                        E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
"""
try:
    loop = True
    while loop:
        n = int(input('Informe um numero inteiro positivo: '))

        if n > 0:
            loop = False
            contador = 1
            e = 1
            while contador <= n:
                e = e + 1/contador
                contador = contador + 1

            print(f'E = {e:.2f}')

except ValueError:
    print('O formato de valor informado esta invalido!')
