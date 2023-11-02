"""
Peca ao usuario para digitar dez valores numericos e ordene por ordem crescente esses
valores, guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao
final na tela os valores em ordem.
"""
try:
    loop = True
    contador = 1
    vet = []
    while loop:
        n = float(input(f'Informe o {contador}º numero: '))
        vet.append(n)

        if contador == 10:
            loop = False
            vet.sort()

            for i in vet:
                print(i, end=' ')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
