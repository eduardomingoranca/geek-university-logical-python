"""
Escreva o menu de opcoes abaixo. Leia a opcao do usuario e execute a operacao escolhida.
Escreva uma mensagem de erro se a opcao for invalida.

Escolha a opcao:
1 - Soma de 2 numeros.
2 - Diferenca entre 2 numeros (maior pelo menor).
3 - Produto entre 2 numeros.
4 - Divisao entre 2 numeros (o denominador nao pode ser zero).
Opcao
"""
try:
    loop = True
    while loop:
        print('===================')
        print('| [1] - SOMA      |')
        print('| [2] - DIFERENCA |')
        print('| [3] - PRODUTO   |')
        print('| [4] - DIVISAO   |')
        print('===================')

        opcao = int(input('Selecione uma opcao: '))

        if 1 <= opcao <= 4:
            numero_um = float(input('Numero 1: '))
            numero_dois = float(input('Numero 2: '))

            if opcao == 1:
                print(f'{numero_um} + {numero_dois} = {numero_um + numero_dois}')
            elif opcao == 2:
                if numero_um > numero_dois:
                    print(f'{numero_um} - {numero_dois} = {numero_um - numero_dois}')
                elif numero_dois > numero_um:
                    print(f'{numero_dois} - {numero_um} = {numero_dois - numero_um}')
            elif opcao == 3:
                print(f'{numero_um} x {numero_dois} = {numero_um * numero_dois}')
            elif opcao == 4:
                if numero_um == 0 or numero_dois == 0:
                    print('NUMERO NAO PODE SER ZERO')
                else:
                    print(f'{numero_um} ÷ {numero_dois} = {numero_um / numero_dois}')
        else:
            loop = False
            print('OPCAO INVALIDA!')

except ValueError:
    print('O valor informado esta invalido!')
