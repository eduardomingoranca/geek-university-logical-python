"""
Faca um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
e imprima a media geral.
"""
try:
    loop = True
    contador = 1
    notas = []
    while loop:
        nota = float(input(f'Informe a nota do {contador}ª aluno: '))
        notas.append(nota)

        if contador == 15:
            loop = False
            soma = 0
            for i in notas:
                soma = soma + i

            print(f'A MEDIA DAS NOTAS DOS {contador} ALUNOS: {soma / contador}')

        contador = contador + 1

except ValueError:
    print('FORMATO INVALIDO!')
