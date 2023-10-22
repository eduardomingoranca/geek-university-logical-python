"""
Dados n e dois numeros inteiros positivos, i e j, diferentes de 0, imprimir em ordem
crescente os n primeiros naturais que sao multiplos de i ou de j e ou de ambos.
"""
try:
    loop = True
    while loop:
        n = int(input('N: '))
        i = int(input('I: '))
        j = int(input('J: '))

        if n > 0 and i > 0 and j > 0:
            loop = False
            contador = 0
            while contador <= n:
                if contador % i == 0 or contador % j == 0 or contador % i == 0 and contador % j == 0:
                    print(contador)
                contador = contador + 1

except ValueError:
    print('O formato de valor informado esta invalido!')
