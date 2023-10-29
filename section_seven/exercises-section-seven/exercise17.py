"""
Leia um vetor de 10 posicoes e atribua valor 0 para todos os elementos que possuirem
valores negativos.
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

            for i in lista:
                if i < 0.0:
                    i = 0.0
                print(f'{i}', end=' ')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
