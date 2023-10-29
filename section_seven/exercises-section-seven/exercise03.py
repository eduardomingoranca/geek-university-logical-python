"""
Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado dos
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos tem
10 elementos cada. Imprimir todos os conjuntos
"""
try:
    loop = True
    v1 = []
    v2 = []
    c1 = {}
    c2 = {}
    contador = 1
    while loop:
        if contador <= 10:
            n = float(input(f'Informe o {contador}º numero: '))
            v1.append(n)
            c1 = set(v1)
        else:
            loop = False

            for i in v1:
                v2.append(pow(i, 2.0))
                c2 = set(v2)

            for i in c1:
                print(i)
            
            print('======================')
            for j in c2:
                print(j)

        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
