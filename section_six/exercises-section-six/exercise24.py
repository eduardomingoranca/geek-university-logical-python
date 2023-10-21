"""
Escreva um programa que leia um numero inteiro e calcule a soma de todos os divisores
desse numero, com excecao dele proprio. Ex: a soma dos divisores do numero 66 eh
1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""
try:
    n = int(input('Informe um numero inteiro: '))

    soma = 0
    if n > 0:
        contador = 1
        while contador < n:
            if n % contador == 0:
                soma = soma + contador
            contador = contador + 1

    print(f'SOMA: {soma}')
except ValueError:
    print('O formato de valor informado esta invalido!')
