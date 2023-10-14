"""
Leia quatro notas, calcule a media aritmetica e imprima o resultado.
"""
numbers = [1, 2, 3, 4]
soma_media = 0
for number in numbers:
    try:
        nota = float(input(f'Informe a {number}ª nota: '))
        soma_media += nota
    except ValueError:
        print('O valor informado esta incorreto!')

media_aritmetica = soma_media / 4.0
print(f'A media aritmetica das notas {media_aritmetica}')
