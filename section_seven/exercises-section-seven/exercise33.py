"""
Faca um programa que leia um vetor de 15 posicoes e o compacte, ou seja, elimine as
posicoes com valor zero. Para isso, todos os elementos a frente do valor zero, devem ser
movidos uma posicao para tras no vetor.
"""
try:
    loop = True
    contador = 1
    vet = []
    while loop:
        vet.append(float(input(f'VET[{contador}]: ')))

        if contador == 15:
            loop = False
            for i in vet:
                if i != 0:
                    print(i, end=' ')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
