"""
Faca um programa que apresente um menu de opcoes para o calculo das seguintes
operacoes entre dois numeros:
    <> adicao (opcao 1)
    <> subtracao (opcao 2)
    <> multiplicacao (opcao 3)
    <> divisao (opcao 4)
    <> saida (opcao 5)
O programa deve possibilitar ao usuario a escolha da operacao desejada, e exibicao do
resultado e a volta ao menu de opcoes. O programa so termina quando for escolhido a
opcao de saida (opcao 5)
"""
try:
    loop = True
    while loop:
        print('=======================')
        print('| [1] - ADICAO        |')
        print('| [2] - SUBTRACAO     |')
        print('| [3] - MULTIPLICACAO |')
        print('| [4] - DIVISAO       |')
        print('| [5] - SAIDA         |')
        print('=======================')

        opcao = int(input('Selecione uma opcao: '))

        if opcao == 1:
            numero_um = float(input('N1: '))
            numero_dois = float(input('N2: '))

            print(f'{numero_um} + {numero_dois} = {numero_um + numero_dois}')
        elif opcao == 2:
            numero_um = float(input('N1: '))
            numero_dois = float(input('N2: '))

            print(f'{numero_um} - {numero_dois} = {numero_um - numero_dois}')
        elif opcao == 3:
            numero_um = float(input('N1: '))
            numero_dois = float(input('N2: '))

            print(f'{numero_um} * {numero_dois} = {numero_um * numero_dois}')
        elif opcao == 4:
            numero_um = float(input('N1: '))
            numero_dois = float(input('N2: '))

            print(f'{numero_um} / {numero_dois} = {(numero_um / numero_dois):.2f}')
        elif opcao == 5:
            loop = False
        else:
            print('OPCAO INVALIDA SELECIONE NOVAMENTE!')

except ValueError:
    print('O formato de valor informado esta invalido!')

