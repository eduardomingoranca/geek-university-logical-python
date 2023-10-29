"""
Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor. Imprima
o vetor, o maior elemento e a posicao que ele se encontra.
"""
try:
    loop = True
    contador = 1
    lista = []
    maior = 0
    posicao_maior = 0
    while loop:
        n = int(input(f'Informe o {contador}º numero inteiro: '))
        lista.append(n)

        if contador == 10:
            loop = False
            cont = 0
            tamanho_lista = len(lista)
            while cont < tamanho_lista:
                if lista[cont] > maior:
                    maior = lista[cont]
                    posicao_maior = cont
                cont = cont + 1

            print(f'MAIOR: {maior} | POSICAO MAIOR: {posicao_maior}')
            
        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
