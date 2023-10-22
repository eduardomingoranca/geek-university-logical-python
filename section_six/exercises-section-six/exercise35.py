"""
Faca um programa que some os numeros impares contidos em um intervalo definido
pelo usuario. O usuario define o valor inicial do intervalo e o valor final deste intervalo
e o programa deve somar todos os numeros impares contidos neste intervalo. Caso o
usuario digite um intervalo invalido (comecando por um valor maior que o valor final) deve
ser escrito uma mensagem de erro na tela, 'Intervalo de valores invalido' e o programa
termina. Exemplo de tela de saida: Digite o valor inicial e o valor final 5
10
Soma dos impares neste intervalo: 21
"""
try:
    valor_inicial = int(input('Digite o valor inicial e o valor final: '))
    valor_final = int(input())

    if valor_inicial >= valor_final:
        print('O valor inicial deve ser menor que o valor final!')
    else:
        soma = 0
        while valor_inicial <= valor_final:
            if valor_inicial % 2 != 0:
                soma = soma + valor_inicial
            valor_inicial = valor_inicial + 1

        print(f'Soma dos impares neste intervalo: {soma}')

except ValueError:
    print('O formato de valor informado esta invalido!')
