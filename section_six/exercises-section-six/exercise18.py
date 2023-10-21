"""
Escreva um algoritmo que leia certa quantidade de numeros e imprima o maior deles e
quantas vezes o maior numero foi lido. A quantidade de numeros a serem lidos deve ser
fornecida pelo usuario.
"""
try:
    loop = True
    while loop:
        quantidade = int(input('Informe a quantidade de numeros que serao lidos: '))

        if quantidade >= 1:
            loop = False
            contador = 0
            maior = 0
            quantidade_maior = 0
            lista = []
            while contador < quantidade:
                contador = contador + 1
                n = float(input(f'Informe o {contador}º numero: '))
                lista.append(n)

                if max(lista) > maior:
                    maior = max(lista)
                    quantidade_maior = quantidade_maior + 1

            print(f'MAIOR: {maior} | TOTAL DE VEZES QUE APARECE: {quantidade_maior}')

except ValueError:
    print('O formato de valor informado esta invalido!')
