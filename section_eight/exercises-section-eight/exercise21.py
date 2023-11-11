"""
Escreva uma funcao para determinar a quantidade de numeros primos abaixo N.
"""
import math


def quantidade_primos(numero):
    # Fazemos um loop para percorrer os numeros de 2 ate o valor digitado
    i = 2
    soma = 0
    while i < numero:
        # Fazemos um casting para que nos retorne um numero inteiro
        raiz = int(math.sqrt(i))
        primo = 0

        # Fazemos outro loop para contar os divisiveis
        j = raiz
        while j > 1:
            # Se o numero for divisivel, aumentamos o contador
            if i % j == 0:
                # Aumentamos o contador
                primo = primo + 1
            j = j - 1

        # Dependendo do numero de divisiveis sabemos se eh primo ou nao,
        # se for primo o contador sera 0
        if primo < 1:
            soma = soma + 1
        i = i + 1

    return soma


try:
    loop = True
    while loop:
        n = int(input('Informe um numero inteiro: '))

        if n > 1:
            loop = False
            print(f'Existe {quantidade_primos(n)} numeros primos abaixo de {n}')

except ValueError:
    print('FORMATO INVALIDO!')
