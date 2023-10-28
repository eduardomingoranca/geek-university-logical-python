"""
Elabore um programa que faca leitura de varios numeros, ate que se digite um
numero negativo. O programa tem que retornar o maior e o menor numero lido.
"""
try:
    loop = True
    lista = []

    def buscar_menor(lst):
        i = float("inf")
        for nr in lst:
            if 0 < nr < i:
                i = nr
        return i

    while loop:
        n = float(input('Informe um numero: '))
        lista.append(n)

        maior = 0
        if max(lista) > maior:
            maior = max(lista)

        if n < 0:
            loop = False
            print(f'Maior: {maior}')
            print(f'Menor: {buscar_menor(lista)}')

except ValueError:
    print('O formato de valor informado esta invalido!')
