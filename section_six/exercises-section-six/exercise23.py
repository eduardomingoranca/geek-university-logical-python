"""
Faca um algoritmo que leia um numero positivo e imprima seus divisores.
"""
try:
    loop = True
    while loop:
        n = float(input('Informe um numero positivo: '))

        if n > 0:
            loop = False
            contador = 1
            while contador <= n:
                if n % contador == 0:
                    print(contador)
                contador = contador + 1

except ValueError:
    print('O formato de valor informado esta invalido!')
