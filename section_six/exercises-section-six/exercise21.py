"""
Faca um programa que receba dois numeros. Calcule e mostre:
        <> a soma dos numeros pares desse intervalo de numeros, incluindo os numeros
        digitados;
        <> a multiplicacao dos numeros impares desse intervalo, incluindo os digitados;
"""
try:
    loop = True
    while loop:
        primeiro_numero = int(input('Informe o primeiro numero: '))
        segundo_numero = int(input('Informe o segundo numero: '))

        soma_par = 0
        multiplica_impar = 1
        if segundo_numero > primeiro_numero:
            loop = False
            while segundo_numero >= primeiro_numero:
                if primeiro_numero % 2 == 0:
                    soma_par = soma_par + primeiro_numero
                elif primeiro_numero % 2 != 0:
                    multiplica_impar = multiplica_impar * primeiro_numero

                primeiro_numero = primeiro_numero + 1

            print(f'SOMA DOS PARES: {soma_par}')
            print(f'MULTIPLICACAO DE IMPARES: {multiplica_impar}')

        elif primeiro_numero > segundo_numero:
            loop = False
            while primeiro_numero >= segundo_numero:
                if segundo_numero % 2 == 0:
                    soma_par = soma_par + segundo_numero
                elif segundo_numero % 2 != 0:
                    multiplica_impar = multiplica_impar * segundo_numero

                segundo_numero = segundo_numero + 1

            print(f'SOMA DOS PARES: {soma_par}')
            print(f'MULTIPLICACAO DE IMPARES: {multiplica_impar}')

except ValueError:
    print('O formato de valor informado esta invalido!')
