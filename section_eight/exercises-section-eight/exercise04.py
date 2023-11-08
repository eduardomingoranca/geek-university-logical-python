"""
Faca uma funcao para verificar se um numero eh um quadrado perfeito. Um quadrado
perfeito eh um numero inteiro nao negativo que pode ser expresso como o quadrado de
outro numero inteiro.
"""


def quadrado_perfeito(n):
    i = 1
    while i <= n:
        if pow(i, 2) == n:
            return True
        i = i + 1
    return False


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro: '))

        if numero > 0:
            loop = False
            if quadrado_perfeito(numero):
                print(f'{numero} eh um quadrado perfeito')
            else:
                print(f'{numero} nao eh um quadrado perfeito')

except ValueError:
    print('FORMATO INVALIDO!')
