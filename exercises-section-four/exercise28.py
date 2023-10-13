"""
Faca a leitura de tres valores e apresente como resultado a soma dos quadrados dos
tres valores lidos.
"""
numbers = [1, 2, 3]
soma_quadrado = 0
for number in numbers:
    try:
        valor = int(input(f'Informe o {number}º numero: '))
        soma_quadrado += pow(valor, 2)
    except ValueError:
        print('O valor informado esta incorreto!')

print(f'A soma dos quadrados dos valores informados eh {soma_quadrado}')
