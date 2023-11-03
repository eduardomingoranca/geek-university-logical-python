"""
Leia uma matriz 5 x 5. Leia tambem um valor X. O programa devera fazer uma busca
desse valor na matriz e, ao final, escrever a localizacao (linha e coluna) ou uma
mensagem de 'nao encontrado'
"""
try:
    matriz = [[0 for i in range(5)] for j in range(5)]
    linha_encontrada = 0
    coluna_encontrada = 0

    for linha in range(4):
        for coluna in range(4):
            numero = float(input(f'M[{linha}][{coluna}]: '))
            matriz[linha][coluna] = numero

    loop = True
    nao_encontrado = True
    while loop:
        x = int(input('Informe o valor na matriz que deseja? '))

        for linha in range(4):
            for coluna in range(4):
                if x == matriz[linha][coluna]:
                    loop = False
                    nao_encontrado = False
                    linha_encontrada = linha
                    coluna_encontrada = coluna
                    print(f'{x} se encontra na linha {linha_encontrada} e na coluna {coluna_encontrada}')

        if nao_encontrado:
            print(f'{x} nao encontrado!')

except ValueError:
    print('FORMATO INVALIDO!')
