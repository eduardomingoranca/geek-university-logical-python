"""
Faca um programa para ler 10 numeros DIFERENTES a serem armazenados em um
vetor. Os dados deverao ser armazenados no vetor na ordem que forem sendo lidos,
sendo que caso o usuario digite um numero que ja foi digitado anteriormente, o programa
devera pedir para ele digitar outro numero. Note que cada valor digitado pelo usuario
deve ser pesquisado no vetor, verificando se ele existe entre os numeros que ja foram
fornecidos. Exibir na tela o vetor final que foi digitado.
"""
try:
    vet = []
    aux = []
    i = 0
    while i < 10:
        numero = float(input(f'Informe o {i}º numero: '))
        aux.append(numero)

        n = numero_existente = 0
        while n < i:
            if aux[n] == numero:
                numero_existente = 1
            n = n + 1

        if numero_existente == 1:
            print('NUMERO EXISTENTE!')
        else:
            vet.append(numero)
        i = i + 1

    print(' ')
    for j in vet:
        print(j, end=' ')

except ValueError:
    print('FORMATO INVALIDO!')
