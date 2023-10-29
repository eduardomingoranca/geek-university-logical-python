"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a media dos valores.
"""
try:
    loop = True
    lista = []
    contador = 1
    soma = 0
    while loop:
        n = float(input(f'Informe o {contador}º valor: '))
        lista.append(n)

        if contador == 5:
            loop = False
            print(f'MAIOR: {max(lista)}')
            print(f'MENOR: {min(lista)}')

            for i in lista:
                soma = soma + i

            print(f'MEIDA DOS VALORES INFORMADOS: {soma / contador}')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
