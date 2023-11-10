"""
Faca uma funcao chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando
varios simbolos de igual (Ex: ========). A funcao recebe por parametro quantos sinais
de igual serao mostrados.
"""


def desenha_linha(sinal_igual):
    linha = []
    i = 0
    while i < sinal_igual:
        linha.append('=')
        i = i + 1

    return linha


try:
    loop = True
    while loop:
        sinais = int(input('Informe a quantidade de sinais que serao exibidos: '))

        if sinais > 0:
            loop = False
            for j in desenha_linha(100):
                print(j, end='')

except ValueError:
    print('FORMATO INVALIDO!')

