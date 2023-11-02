"""
Faca um programa que leia dois numeros a e b (positivos menores que 10000) e:
    <> Crie um vetor onde cada posicao eh um algarismo do numero. A primeira posicao eh
    o algarismo menos significativo.
    <> Crie um vetor que seja a soma de a e b, mas faca-o usando apenas os vetores
    construidos anteriormente.
"""
try:
    vet = []
    soma = []
    loop = True
    while loop:
        a = int(input('A: '))
        b = int(input('B: '))

        if a < 10000 or b < 10000:
            loop = False
            if a < b:
                i = a
                while i <= b:
                    vet.append(i)
                    i = i + 1
            elif a > b:
                j = b
                while j <= a:
                    vet.append(j)
                    j = j + 1

            for p in vet:
                print(p, end=' ')

            print(' ')
            k = 0
            while k < len(vet):
                soma.append(vet[k] + vet[k])
                print(soma[k], end=' ')
                k = k + 1

except ValueError:
    print('FORMATO INVALIDO!')
