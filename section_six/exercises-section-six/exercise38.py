"""
Faca um programa que calcule o termo pitagorico a, b, c para o qual a + b + c = 1000. Um
terno pitagorico eh um conjunto de tres numeros naturais, a, b, c, para a qual,
                    a² + b² = c²
Por exemplo,
                    3² + 4² = 9 + 16 = 25 = 5²
"""
try:
    loop = True
    contador = 1
    while loop:
        a = int(input('A: '))
        b = int(input('B: '))
        c = int(input('C: '))

        if (pow(a, 2.0) + pow(b, 2.0)) == pow(c, 2.0):
            loop = False
            print(f'{a}² + {b}² = {c}² | {pow(a, 2.0)} + {pow(b, 2.0)} = {pow(c, 2.0)}')

except ValueError:
    print('O formato de valor informado esta invalido!')
