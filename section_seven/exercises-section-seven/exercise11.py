"""
Faca um programa que preencha um vetor com 10 numeros reais, calcule e mostre a
quantidade de numeros negativos e a soma dos numeros positivos desse vetor.
"""
try:
    loop = True
    contador = 1
    vetor = []
    total_negativos = 0
    soma = 0
    while loop:
        n = float(input(f'Informe o {contador}º valor: '))
        vetor.append(n)

        if contador == 10:
            loop = False
            for i in vetor:
                if i < 0:
                    total_negativos = total_negativos + 1
                else:
                    soma = soma + i

            print(f'QUANTIDADE TOTAL DE NUMEROS NEGATIVOS INFORMADOS {total_negativos}')
            print(f'SOMA TOTAL DOS NUMEROS POSITIVOS INFORMADOS {soma}')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
