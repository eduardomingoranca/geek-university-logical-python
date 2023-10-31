"""
Leia 10 numeros inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores impares de v para v1, e os valores pares de v para v2. Note que cada
um dos vetores v1 e v2 tem no maximo 10 elementos, mas nem todos os elementos sao
utilizados. No final escreva os elementos UTILIZADOS de v1 e v2.
"""
try:
    loop = True
    contador = 1
    v = []
    v1 = []
    v2 = []
    while loop:
        v.append(int(input(f'Informe o {contador}º numero inteiro: ')))

        if contador == 10:
            loop = False

            for i in v:
                if i % 2 != 0:
                    v1.append(i)

            for j in v:
                if j % 2 == 0:
                    v2.append(j)

            for p in v1:
                print(p, end=' ')

            print(' ')
            for s in v2:
                print(s, end=' ')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
