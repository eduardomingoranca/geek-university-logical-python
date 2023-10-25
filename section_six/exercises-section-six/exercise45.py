"""
Faca um algoritmo que converta uma velocidade expressa em km/h para m/s e vice
versa. Voce deve criar um menu com as duas opcoes de conversao e com uma opcao
para finalizar o programa. O usuario podera fazer quantas conversoes desejar,
sendo que o programa so sera finalizado quando a opcao de finalizar for escolhida.
"""
try:
    loop = True
    while loop:
        velociade = float(input('Informe a velocidade: '))

        print('===================================')
        print('| [1] - CONVERTA EM KM/H PARA M/S |')
        print('| [2] - CONVERTA EM M/S PARA KM/H |')
        print('| [3] - SAIR                      |')
        print('===================================')

        opcao = int(input('Selecione uma opcao: '))

        if opcao == 1:
            print(f'velocidade em {velociade} km/h para {(velociade / 3.6):.2f} m/s')
        elif opcao == 2:
            print(f'velocidade em {velociade} m/s para {(velociade * 3.6):.2f} km/h')
        elif opcao == 3:
            loop = False
        else:
            print('VALOR INVALIDO INFORME NOVAMENTE!')

except ValueError:
    print('O formato de valor informado esta invalido!')
