"""
Faca um programa que receba um numero inteiro maior do que 1, e verifique se o numero
fornecido eh primo ou nao.
"""
try:
    loop = True
    while loop:
        n = int(input('Informe um numero inteiro: '))

        if n > 1:
            loop = False
            contador = 1
            primo = 0
            while contador <= n:
                if n % contador == 0:
                    primo = primo + 1
                contador = contador + 1

            if primo == 2:
                print(f'{n} NUMERO PRIMO')
            else:
                print(f'{n} NAO EH NUMERO PRIMO')

except ValueError:
    print('O formato de valor informado esta invalido!')
