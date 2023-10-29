"""
Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
"""
try:
    loop = True
    contador = 0
    lista = []
    while loop:
        contador = contador + 1

        if contador <= 6:
            n = int(input(f'Informe o {contador}º valor inteiro: '))
            lista.append(n)
        else:
            loop = False
            for i in lista:
                print(i)

except ValueError:
    print('FORMATO INVALIDO!')
