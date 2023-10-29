"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posicao onde se encontram
o maior e o menor valor.
"""
try:
    loop = True
    lista = []
    contador = 1
    while loop:
        n = float(input(f'Informe o {contador}º valor: '))
        lista.append(n)

        if contador == 5:
            loop = False
            cont = 0
            maior = max(lista)
            menor = min(lista)
            tamanho_lista = len(lista)
            posicao_maior = 0
            posicao_menor = 0
            while cont < tamanho_lista:
                if lista[cont] == maior:
                    posicao_maior = cont

                if lista[cont] == menor:
                    posicao_menor = cont

                cont = cont + 1

            print(f'MAIOR: {maior} | POSICAO MAIOR: {posicao_maior}')
            print(f'MENOR: {menor} | POSICAO MENOR: {posicao_menor}')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
