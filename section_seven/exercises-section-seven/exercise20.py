"""
Escreva um programa que leia numeros inteiros no intervalo[0,50] e os armazene em um
vetor com 10 posicoes. Preencha um segundo vetor apenas com os numeros impares
do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
"""
try:
    loop = True
    contador = 1
    lista = []
    while loop:
        n = int(input(f'Informe o {contador}º numero inteiro no intervalo[0,50]: '))

        if 0 <= n <= 50:
            lista.append(n)
            if contador == 10:
                loop = False
                lista_impar = []
                for i in lista:
                    if i % 2 != 0:
                        lista_impar.append(i)

                for j in lista_impar:
                    print(f'{j}', end=' ')

                print('')
                for k in lista:
                    print(f'{k}', end=' ')
        else:
            loop = False

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
