"""
Faca um programa que receba 6 numeros inteiros e mostre:
    <> Os numeros pares digitados;
    <> A soma dos numeros pares digitados;
    <> Os numeros impares digitados;
    <> A quantidade de numeros impares digitados;
"""
try:
    loop = True
    vet = []
    contador = 1
    par = 0
    soma_par = 0
    total_impar = 0
    while loop:
        vet.append(int(input(f'Informe o {contador}º numero inteiro: ')))

        if contador == 6:
            loop = False
            for i in vet:
                if i % 2 == 0:
                    print(i, end=' ')
                    soma_par = soma_par + i

            print('')
            for j in vet:
                if j % 2 != 0:
                    print(j, end=' ')
                    total_impar = total_impar + 1

            print('')
            print(f'SOMA PAR: {soma_par} | QUANTIDADE TOTAL DE IMPARES INFORMADOS: {total_impar}')

        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
