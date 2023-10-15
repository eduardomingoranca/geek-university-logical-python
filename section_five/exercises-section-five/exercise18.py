"""
Faca um programa que mostre ao usuario um menu com 4 opcoes de operacoes matematicas
(as basicas, por exemplo). O usuario escolhe uma das opcoes e o seu programa entao
pede dois valores numericos e realiza a operacao, mostrando o resultado e saindo.
"""
try:
    loop = True
    while loop:
        print('=======================')
        print('| [1] - ADICAO        |')
        print('| [2] - SUBTRACAO     |')
        print('| [3] - MULTIPLICACAO |')
        print('| [4] - DIVISAO       |')
        print('=======================')

        opcao = int(input('Informe uma opcao: '))

        if 1 <= opcao <= 4:
            numero_um = float(input('Numero 1: '))
            numero_dois = float(input('Numero 2: '))

            if opcao == 1:
                print(f'{numero_um} + {numero_dois} = {numero_um + numero_dois}')
            elif opcao == 2:
                print(f'{numero_um} - {numero_dois} = {numero_um - numero_dois}')
            elif opcao == 3:
                print(f'{numero_um} x {numero_dois} = {numero_um * numero_dois}')
            elif opcao == 4:
                print(f'{numero_um} ÷ {numero_dois} = {numero_um / numero_dois}')
        else:
            loop = False
            print('OPCAO INVALIDA!')

except ValueError:
    print('O valor informado esta invalido!')
