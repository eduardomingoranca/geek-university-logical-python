"""
Leia dois conjuntos de numeros reais, armazenando-os em vetores e calcular o produto
escalar entre eles. Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos e o
produto escalar, sendo que o produto escalar eh dado por: x1 * y1 + x2 * y2 + ... + xn * yn
"""
try:
    loop = True
    a = []
    b = []
    p = []
    contador = 0
    indice = 0
    while loop:
        a.append(float(input('A: ')))
        b.append(float(input('B: ')))
        x = set(a)
        y = set(b)

        if contador == 4:
            loop = False
            print('')
            for i in x:
                print(i, end=' ')

            print('')
            for j in y:
                print(j, end=' ')

            a1 = list(a)
            b1 = list(b)
            while indice < 5:
                p.append(a1[indice] * b1[indice])
                indice = indice + 1

            print('')
            for c in p:
                print(c, end=' ')

        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
