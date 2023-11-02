"""
Leia um vetor com 10 numeros reais, ordene os elementos deste vetor, e no final escreva
os elementos do vetor ordenado.
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
