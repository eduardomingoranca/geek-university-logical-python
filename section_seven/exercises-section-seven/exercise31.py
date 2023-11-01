"""
Faca um programa que leia dois vetores de 10 elementos. Crie um vetores que seja a uniao
entre os 2 vetores anteriores, ou seja, que contem os numeros dos dois vetores. Nao
deve conter numeros repetidos.
"""
try:
    loop = True
    v1 = []
    v2 = []
    uniao = []
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

            b = 0
            while b < 10:
                if v1[b] != v2[b]:
                    uniao.append(v1[b])
                    uniao.append(v2[b])
                b = b + 1

            for i in uniao:
                print(i, end=' ')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
