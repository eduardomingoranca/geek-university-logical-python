"""
Escreva um programa que leia o numero de habitantes de uma determinada cidade, o
valor do kwh, e para cada habitante entre com os seguintes dados: consumo de mes
e o codigo do consumidor (1 - Residencial, 2 - Comercial, 3 - Industrial). No final imprima o
maior, o menor e a media do consumo dos habitantes; e por fim o total do consumo de
cada categoria de consumidor.
"""
try:
    loop = True
    while loop:
        numero_habitantes = int(input('Informe o numero de habitantes da cidade: '))
        valor_kwh = float(input('Informe o valor do kwh - R$ '))

        if numero_habitantes >= 1:
            loop = False
            contador = 0
            lista = []
            soma = 0
            maior = 0
            menor = 0
            total_residencial = 0
            total_comercial = 0
            total_industrial = 0
            while contador < numero_habitantes:
                print('=====================')
                print('| [1] - RESIDENCIAL |')
                print('| [2] - COMERCIAL   |')
                print('| [3] - INDUSTRIAL  |')
                print('=====================')

                codigo_consumidor = int(input('Selecione o codigo do consumidor: '))

                if 1 <= codigo_consumidor <= 3:
                    consumo_mes = float(input('Informe o consumo mensal de kwh: '))

                if codigo_consumidor == 1:
                    lista.append(consumo_mes)
                    total_residencial = total_residencial + consumo_mes
                elif codigo_consumidor == 2:
                    lista.append(consumo_mes)
                    total_comercial = total_comercial + consumo_mes
                elif codigo_consumidor == 3:
                    lista.append(consumo_mes)
                    total_industrial = total_industrial + consumo_mes

                maior = max(lista)
                menor = min(lista)
                soma = soma + consumo_mes
                contador = contador + 1

            print(f'MAIOR: {maior} | MENOR: {menor}')
            print(f'MEDIA DE CONSUMO : {soma / contador}')
            print(f'T0TAL CONSUMO RESIDENCIAL: {total_residencial}')
            print(f'T0TAL CONSUMO COMERCIAL: {total_comercial}')
            print(f'T0TAL CONSUMO INDUSTRIAL: {total_industrial}')

except ValueError:
    print('O formato de valor informado esta invalido!')
