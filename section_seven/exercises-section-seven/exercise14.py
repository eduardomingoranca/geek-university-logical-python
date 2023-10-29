"""
Faca um programa que leia um vetor de 10 posicoes e verifique se existem valores iguais
e os escreva na tela.
"""


def copy_of(lst, length):
    out = lst.copy()
    out[length:] = [0 for _ in range(length - len(lst))]
    return out


try:
    loop = True
    contador = 1
    lista = []
    while loop:
        n = float(input(f'Informe o {contador}º valor: '))
        lista.append(n)

        if contador == 10:
            loop = False

            i = 0
            n1 = len(lista)
            aux = copy_of(lista, n1)  # copiando o vetor
            while i < n1:
                # verificando para cada item removido, se o item na posicao i
                # ja se encontra em alguma posicao a frente no vetor, se o elemento se encontrar
                # remover do vetor aux
                k = i + 1
                removidos = 0
                j = i + 1
                while j < n1:
                    if aux[j] == aux[i]:
                        removidos = removidos + 1
                    else:
                        aux[k] = aux[j]
                        k = k + 1
                    j = j + 1

                n1 = n1 - removidos
                i = i + 1

            aux = copy_of(aux, n1)

            for auxiliar in aux:
                print(f'{auxiliar}')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
