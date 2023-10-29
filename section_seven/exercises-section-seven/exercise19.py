"""
Faca um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i) % (i + 1), sendo
i a posicao do elemento no vetor. Em seguida imprima o vetor na tela.
"""
loop = True
vetor = []
i = 0
while loop:
    vetor.append((i + 5 * i) % (i + 1))

    if i == 50:
        loop = False
        for j in vetor:
            print(f'{j}', end=' ')

    i = i + 1
