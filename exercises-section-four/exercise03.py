"""
Peca ao usuario para digitar tres valores inteiros e imprima a soma deles.
"""
numbers = [1, 2, 3]
soma = 0
for number in numbers:
    try:
        numero = int(input(f'Informe o {number}º valor inteiro: '))
        soma += numero
    except ValueError:
        print('O valor esta invalido!')

print(f'A soma dos valores eh {soma}')
