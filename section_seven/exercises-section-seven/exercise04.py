"""
Faca um programa que leia um vetor de 8 posicoes e, em seguida, leia tambem dois valores
X e Y quaisquer correspondentes a duas posicoes no vetor. Ao final seu programa devera
escrever a soma dos valores encontrados nas respectivas posicoes X e Y
"""
try:
    loop = True
    contador = 1
    lista = []
    while loop:
        n = float(input(f'Informe o {contador}º valor: '))
        lista.append(n)

        if contador >= 8:
            loop = False
            rep1 = True
            rep2 = True
            tamanho_lista = len(lista)
            n1 = 0
            n2 = 0

            while rep1:
                x = int(input('X: '))

                if 0 <= x < tamanho_lista:
                    rep1 = False
                    n1 = lista[x]

            while rep2:
                y = int(input('Y: '))

                if 0 <= y < tamanho_lista:
                    rep2 = False
                    n2 = lista[y]
                    print(f'{n1} + {n2} = {n1 + n2}')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
