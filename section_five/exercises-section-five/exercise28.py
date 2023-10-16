"""
Faca um programa que leia tres numeros inteiros positivos e efetue o calculo de uma das
seguintes medias de acordo com um valor numerico digitado pelo usuario:
            (a) Geometrica: \³/x * y * z
            (b) Ponderada: x + 2 * y + 3 * z / 6
            (c) Harmonica: 1 / 1/x + 1/y + 1/z
            (d) Aritmetica: x + y + z / 3
"""
try:
    loop = True
    while loop:
        print('=======================================')
        print('| [1] - Geometrica | [2] - Ponderada  |')
        print('| [3] - Harmonica  | [4] - Aritmetica |')
        print('=======================================')

        opcao = int(input('Selecione uma opcao: '))

        if 1 <= opcao <= 4:
            x = int(input('X: '))
            y = int(input('Y: '))
            z = int(input('Z: '))

            if opcao == 1:
                print(f'Geometrica: \³/{x} * {y} * {z}')
                print(f'Geometrica: {((x * y * z) ** (1/3)):.2f}')
            elif opcao == 2:
                print(f'Ponderada: {x} + 2 * {y} + 3 * {z} / 6')
                print(f'Ponderada: {(x + 2 * y + 3 * z / 6):.2f}')
            elif opcao == 3:
                print(f'Harmonica: 1 / 1/{x} + 1/{y} + 1/{z}')
                print(f'Harmonica: {(1 / 1/x + 1/y + 1/z):.2f}')
            elif opcao == 4:
                print(f'Aritmetica: {x} + {y} + {z} / 3')
                print(f'Aritmetica: {(x + y + z / 3):.2f}')
        else:
            loop = False
            print('OPCAO INVALIDA!')

except ValueError:
    print('O valor informado esta invalido!')
