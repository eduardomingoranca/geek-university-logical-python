"""
Faca um programa que receba do usuario vetores, A e B, com 10 numeros inteiros
cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados
do vetor C.
"""
try:
    loop = True
    a = []
    b = []
    c = []
    contador = 1
    while loop:
        a.append(int(input(f'A[{contador}]: ')))
        b.append(int(input(f'B[{contador}]: ')))

        if contador == 10:
            loop = False

            indice = 0
            while indice < len(a):
                c = a[indice] - b[indice]
                print(f'{c}', end=' ')
                indice = indice + 1

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
