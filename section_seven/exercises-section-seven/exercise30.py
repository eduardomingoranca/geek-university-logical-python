"""
Faca um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a
interseccao entre os 2 vetores anteriores, ou seja, que contem apenas os numeros que
estao em ambos os vetores. Nao deve conter numeros repetidos.
"""
try:
    loop = True
    v1 = []
    v2 = []
    interseccao = []
    contador = 1
    while loop:
        v1.append(float(input(f'V1[{contador}]: ')))
        v2.append(float(input(f'V2[{contador}]: ')))

        if contador == 10:
            loop = False

            aux = set(v1)
            aux2 = set(v2)

            for i in aux:
                v1.append(i)

            for j in aux2:
                v2.append(j)

            a = 0
            while a < 10:
                if v1[a] == v2[a]:
                    interseccao.append(v1[a])
                a = a + 1

            for i in interseccao:
                print(i, end=' ')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
