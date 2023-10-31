"""
Leia 10 numeros inteiros e armazene em um vetor. Em seguida escreva os elementos
que sao primos e suas respectivas posicoes no vetor.
"""


def eh_primo(numero):
    j = 2
    while j < numero:
        if numero % j == 0:
            return False
        j = j + 1

    return True


try:
    loop = True
    v = []
    contador = 1
    while loop:
        v.append(int(input(f'Informe o {contador}º numero inteiro: ')))

        if contador == 10:
            loop = False

            primo = True
            for i in v:
                if eh_primo(i):
                    print(i, end=' ')

        contador = contador + 1
except ValueError:
    print('FORMATO INVALIDO!')
