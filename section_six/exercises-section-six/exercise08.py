"""
Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor
lido
"""
try:
    contador = 0
    menor = 0
    maior = 0
    lista = []
    while contador < 10:
        contador = contador + 1
        numero = int(input(f'Informe o {contador}º numero: '))
        lista.append(numero)

        menor = min(lista)
        maior = max(lista)

    print(f'MENOR: {menor} | MAIOR: {maior}')
except ValueError:
    print('O formato de valor informado esta invalido!')
