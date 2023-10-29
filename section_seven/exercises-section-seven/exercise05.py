"""
Leia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui.
"""
try:
    loop = True
    contador = 1
    lista = []
    while loop:
        n = float(input(f'Informe o {contador}º numero: '))
        lista.append(n)

        if contador == 10:
            loop = False
            pares = 0
            for i in lista:
                if i % 2 == 0 and i != 0:
                    pares = pares + 1

            print(f'TOTAL DE VALORES PARES: {pares}')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
