"""
Faca um programa que leia dez conjuntos de dois valores, o primeiro representando o
numero do aluno e o segundo representando a sua altura em metros. Encontre o aluno
mais baixo e o mais alto. Mostre o numero do aluno mais baixo e do mais alto, juntamente
com suas alturas.
"""
try:
    loop = True
    contador = 1
    a = []
    b = []
    while loop:
        numero_aluno = int(input(f'Informe o numero do {contador}ª aluno: '))
        altura_aluno = float(input(f'Informe a altura do {contador}º aluno: '))
        a.append(numero_aluno)
        b.append(altura_aluno)

        if contador == 5:
            loop = False
            c = set(a)
            d = set(b)

            e = list(c)
            f = list(d)

            indice = 0
            maior_altura = 0
            maior_numero_aluno = 0
            i = 0
            while indice < len(f):
                if f[indice] > maior_altura:
                    maior_altura = f[indice]
                    i = indice
                indice = indice + 1

            j = 0
            while j <= i:
                if j == i:
                    maior_numero_aluno = e[j]
                j = j + 1

            ind = 0
            menor_altura = maior_altura
            menor_numero_aluno = 0
            k = 0
            while ind < len(f):
                if f[ind] < menor_altura:
                    menor_altura = f[ind]
                    k = ind
                ind = ind + 1

            p = 0
            while p <= k:
                if p == k:
                    menor_numero_aluno = e[p]
                p = p + 1

            print(f'MAIS ALTO: {maior_altura} | NUMERO ALUNO MAIS ALTO: {maior_numero_aluno}')
            print(f'MAIS BAIXO: {menor_altura} | NUMERO ALUNO MAIS BAIXO: {menor_numero_aluno}')

        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
