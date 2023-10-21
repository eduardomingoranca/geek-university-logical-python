"""
Ler uma sequencia de numeros inteiros e determine se eles sao pares ou nao. Devera
ser informado o numero de dados lidos e numero de valores pares. O processo termina
quando for digitado o numero 1000.
"""
try:
    loop = True
    par = 0
    quantidade_numero = 0

    while loop:
        n = int(input('Informe o numero (1000 para parar): '))

        if n != 1000:
            if n % 2 == 0:
                par = par + 1

            quantidade_numero = quantidade_numero + 1

        if n == 1000:
            loop = False
            print(f'TOTAL DE NUMEROS PARES: {par}')
            print(f'TOTAL DE NUMEROS INFORMADOS: {quantidade_numero}')

except ValueError:
    print('O formato de valor informado esta invalido!')
