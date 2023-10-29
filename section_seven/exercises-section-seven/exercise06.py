"""
Faca um programa que rebeca do usuario um vetor com 10 posicoes. Em seguida devera
ser impresso o maior e o menor elemento do vetor.
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
            print(f'MAIOR: {max(lista)}')
            print(f'MENOR: {min(lista)}')

        contador = contador + 1


except ValueError:
    print('FORMATO INVALIDO!')
