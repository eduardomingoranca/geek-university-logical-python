"""
Faca um programa que leia um vetor de 5 posicoes para numeros reais e, depois, um
codigo inteiro. Se o codigo for zero, finalize o programa; se for 1, mostre o vetor na ordem
direta; se for 2, mostre o vetor na ordem inversa. Caso, o codigo for diferente de 1 e 2
escreva uma mensagem informando que o codigo eh invalido.
"""
try:
    loop = True
    contador = 1
    lista = []
    while loop:
        n = float(input(f'Informe o {contador}º numero: '))
        lista.append(n)

        if contador == 5:
            loop = False
            rep = True
            while rep:
                print('')
                print('=============================')
                print('| [0] - FINALIZA O PROGRAMA |')
                print('| [1] - VETOR ORDEM DIRETA  |')
                print('| [2] - VETOR ORDEM INVERSA |')
                print('=============================')

                codigo = int(input('Selecione uma opcao: '))

                if codigo == 0:
                    rep = False
                elif codigo == 1:
                    for i in lista:
                        print(f'{i}', end=' ')
                elif codigo == 2:
                    lista.reverse()
                    for i in lista:
                        print(f'{i}', end=' ')
                else:
                    print('OPCAO INVALIDA!')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
