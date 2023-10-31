"""
Faca um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais
que nao sao multiplos de 7 ou que terminam com 7.
"""
loop = True
contador = 0
v1 = []
while loop:
    v1.append(contador)

    if contador == 99:
        loop = False

        for i in v1:
            if i % 7 == 0:
                print(i, end=' ')

    contador = contador + 1
