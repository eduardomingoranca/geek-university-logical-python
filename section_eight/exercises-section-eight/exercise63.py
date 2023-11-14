"""
Crie uma funcao que compara duas strings e que retorna se elas sao iguais ou diferentes.
"""


def comparacao(p1, p2):
    if p1 == p2:
        return True

    return False


try:
    loop = True
    while loop:
        palavra1 = input('Informe uma palavra: ')
        palavra2 = input('Informe outra palavra: ')

        comp = comparacao(palavra1, palavra2)

        if comp:
            loop = False
            print(f'As palavras {palavra1} e {palavra2} sao iguais')

except ValueError:
    print('FORMATO INVALIDO!')
