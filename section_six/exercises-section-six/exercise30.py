"""
Faca programas para calcular as seguintes sequencias:
        1 + 2 + 3 + 4 + 5 + ... + n
        1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
        1 + 3 + 5 + 7 + ... + (2n - 1)
"""
try:
    n = int(input('Informe um numero inteiro: '))

    contador = 1
    s1 = 0
    s2 = 0
    s3 = 0
    while contador <= n:
        s1 = s1 + contador
        s2 = s2 + contador - (contador + 1)
        s3 = s3 + contador * 2
        contador = contador + 1

    print(f'S1: {s1}')
    print(f'S2: {s2}')
    print(f'S3: {s3}')

except ValueError:
    print('O formato de valor informado esta invalido!')
