"""
Faca um programa que leia varios numeros, calcule e mostre:
    (a) A soma dos numeros digitados
    (b) A quantidade de numeros digitados
    (c) A media dos numeros digitados
    (d) O maior numero digitado
    (e) O menor numero digitado
    (f) A media dos numeros pares
Finalize a entrada de dados caso o usuario informe o valor 0.
"""
try:
    loop = True
    soma = 0
    quantidade = 0
    soma_par = 0
    lista = []
    maior = 0
    menor = 0
    quantidade_par = 0
    while loop:
        n = float(input('Informe um numero (ZERO para Finalizar): '))

        if n != 0:        
            lista.append(n)
            maior = max(lista)
            menor = min(lista)

            quantidade = quantidade + 1
            soma = soma + n

            if n % 2 == 0:
                soma_par = soma_par + n
                quantidade_par = quantidade_par + 1
        else:
            loop = False
            print(f'SOMA DOS NUMEROS INFORMADOS: {soma}')
            print(f'TOTAL DE NUMEROS INFORMADOS: {quantidade}')
            print(f'MEDIA DOS NUMEROS INFORMADOS: {soma / quantidade}')
            print(f'MAIOR NUMERO INFORMADO: {maior}')
            print(f'MENOR NUMERO INFORMADO: {menor}')
            print(f'MEDIA DOS NUMEROS PARES: {soma_par / quantidade_par}')

except ValueError:
    print('O formato de valor informado esta invalido!')
