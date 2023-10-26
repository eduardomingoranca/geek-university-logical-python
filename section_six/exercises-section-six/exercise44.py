"""
Leia um numero positivo do usuario, entao, calcule e imprima a sequencia Fibonacci ate
o primeiro numero superior ao numero lido. Exemplo: se o usuario informou o numero 30,
a sequencia a ser impressa sera 0 1 1 2 3 5 8 13 21.
"""
try:
    loop = True
    while loop:
        n = int(input('Informe um numero positivo: '))

        if n > 0:
            loop = False
            anterior = 0
            proximo = 1
            while anterior < n:
                print(f'{anterior}')
                fibonacci = anterior + proximo
                anterior = proximo
                proximo = fibonacci

except ValueError:
    print('O formato de valor informado esta invalido!')
