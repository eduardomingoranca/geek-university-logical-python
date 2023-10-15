"""
Faca um algoritmo que calcule a media ponderada das notas de 3 provas. A primeira e
a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a media do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovacao deve ser igual ou
superior a 60 pontos.
"""
try:
    nota_um = float(input('nota 01: '))
    nota_dois = float(input('nota 02: '))
    nota_tres = float(input('nota 03: '))

    media_ponderada = (nota_um * 1.00 + nota_dois * 1.00 + nota_tres * 2.00) / 3.0

    if media_ponderada >= 60:
        print(f'media: {media_ponderada}')
        print('APROVADO')
    else:
        print(f'media: {media_ponderada}')
        print('REPROVADO')

except ValueError:
    print('O valor informado esta invalido!')
