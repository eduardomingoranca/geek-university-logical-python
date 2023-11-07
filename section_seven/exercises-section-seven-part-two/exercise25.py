"""
Faca um programa para determinar a proxima jogada em um Jogo da Velha. Assumir que
o tabuleiro eh representado por uma matriz de 3 x 3, onde cada posicao representa uma
das casas do tabuleiro. A matriz pode conter os seguintes valores -1, 0, 1 representando
respectivamente uma casa contendo uma peca minha (-1), uma casa vazia do tabuleiro (0),
e uma casa contendo uma peca do meu oponente (1).
Exemplo:
        | -1 |  1 | 1 |
        | -1 | -1 | 0 |
        | 0  |  1 | 0 |
"""
try:
    jogo_velha = [[0 for i in range(3)] for j in range(3)]

    print('========================')
    print('    JOGO DA VELHA       ')
    print('========================')

    for linha in range(3):
        for coluna in range(3):
            scanner = int(input(f'JOGO DA VELHA [{linha}][{coluna}]: '))
            jogo_velha[linha][coluna] = scanner

    for linha in range(3):
        for coluna in range(3):
            print(f'{jogo_velha[linha][coluna]}', end=' ')
        print('')

    print(' ')
    for linha in range(3):
        for coluna in range(3):
            if linha == coluna or linha + coluna == len(jogo_velha) -1:
                if jogo_velha[linha][coluna] == 1:
                    print('VENCEDOR[1]')
                elif jogo_velha[linha][coluna] == -1:
                    print('VENCEDOR[-1]')
            break

except ValueError:
    print('FORMATO INVALIDO!')
