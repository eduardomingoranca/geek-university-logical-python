"""
Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuario nao
informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso
baixo:
        <> Soma entre x e y: soma de cada elemento de x com o elemento da mesma posicao
           em y.
        <> Produto entre x e y: multiplicacao de cada elemento de x com o elemento da mesma
           posicao em y.
        <> Diferenca entre x e y: todos os elementos de x que nao existam em y.
        <> Interseccao entre x e y: apenas elementos que aparecem nos dois vetores
        <> Uniao entre x e y: todos os elementos x, e todos os elementos de y que nao
        estao em x.
"""
try:
    loop = True
    x = []
    y = []
    soma = []
    produto = []
    diferenca = []
    interseccao = []
    uniao = []
    contador = 1
    print('INFORME NUMEROS INTEIROS!')
    while loop:
        x.append(int(input(f'X[{contador}]: ')))
        y.append(int(input(f'Y[{contador}]: ')))

        if contador == 5:
            loop = False

            aux = set(x)
            aux2 = set(y)

            for i in aux:
                x.append(i)

            for j in aux2:
                y.append(j)

            a = 0
            while a < 5:
                soma.append(x[a] + y[a])
                produto.append(x[a] - y[a])

                if x[a] != y[a]:
                    diferenca.append(x[a])
                    uniao.append(x[a])
                    uniao.append(y[a])

                if x[a] == y[a]:
                    interseccao.append(x[a])
                a = a + 1

            for i in soma:
                print(i, end=' ')

            print('')
            for j in produto:
                print(j, end=' ')

            print('')
            for i in diferenca:
                print(i, end=' ')

            print('')
            for j in interseccao:
                print(j, end=' ')

            print('')
            for i in uniao:
                print(i, end=' ')

        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
