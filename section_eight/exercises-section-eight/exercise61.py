"""
Escreva uma funcao que compare e retorne verdadeiro, caso uma string seja anagrama
da outra, e falso, caso contrario.
"""


def anagrama(p1, p2):
    if p1[::-1] == p2:
        return True

    return False


try:
    loop = True
    while loop:
        palavra1 = input('Informe uma palavra: ')
        palavra2 = input('Informe outra palavra: ')

        anag = anagrama(palavra1, palavra2)

        if anag:
            loop = False
            print(f'A palavra {palavra2} eh anagrama da palavra {palavra1}')

except ValueError:
    print('FORMATO INVALIDO!')
