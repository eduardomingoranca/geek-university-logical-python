"""
Elabore uma funcao que receba tres notas de um aluno como parametros e uma letra.
Se a letra for A, a funcao devera calcular a media aritmetica das notas do aluno;
se for P, devera calcular a media ponderada, com pesos 5, 3 e 2.
"""


def media_notas(n1, n2, n3, lt):
    if lt == 'A' or lt == 'a':
        return (n1 + n2 + n3) / 3.0
    elif lt == 'P' or lt == 'p':
        return (n1 * 5 + n2 * 3 + n3 * 2) / (5 + 3 + 2)


try:
    loop = True
    while loop:
        x = float(input('Informe o 1º numero: '))
        y = float(input('Informe o 2º numero: '))
        z = float(input('Informe o 3º numero: '))
        letra = input('Informe uma letra (A / P): ')

        if letra == 'A' or letra == 'a':
            loop = False
            print(f'Media Aritmetica: {media_notas(x, y, z, letra)}')
        elif letra == 'P' or letra == 'p':
            loop = False
            print(f'Media Ponderada: {media_notas(x, y, z, letra)}')

except ValueError:
    print('FORMATO INVALIDO!')
