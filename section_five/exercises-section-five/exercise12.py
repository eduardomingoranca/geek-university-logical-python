"""
Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem 'Numero
invalido'. Se o numero for positivo, calcular o logaritmo deste numero.
"""
try:
    numero = int(input('Informe um numero inteiro: '))

    loop = True
    contador = 0

    if numero > 0:
        a = numero / 3
        while loop:
            if a == 1:
                contador = contador + 1
                print(f'X = {contador}')
                loop = False
            else:
                a = a / 3
                contador = contador + 1
    else:
        print('NUMERO INVALIDO!')

except ValueError:
    print('O valor informado esta invalido!')
