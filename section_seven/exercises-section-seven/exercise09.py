"""
Crie um programa que le 6 valores inteiros pares e, em seguida, mostre na tela os valores
lidos na ordem inversa.
"""
try:
    loop = True
    contador = 1
    lista = []
    while loop:
        n = int(input(f'Informe o {contador}º valor inteiros: '))

        if n % 2 == 0:
            lista.append(n)
            if contador == 6:
                loop = False
                lista.reverse()
                for i in lista:
                    print(i, end=' ')

        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
