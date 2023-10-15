"""
A nota final de um estudante eh calculada a partir de tres notas atribuidas entre o intervalo
de 0 ate 10, respectivamente, a um trabalho de laboratoria, a uma avaliacao semestral e a um
exame final. A media das tres notas mencionadas anteriormente obedece aos pesos: Trabalho de
Laboratorio: 2; Avaliacao Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na
tela se o aluno esta reprovado (media entre 0 e 2.9), de recuperacao (entre 3 e 4.9) ou se foi
aprovado. Faca todas as verificacoes necessarias.
"""
try:
    nota_trabalho_laboratoria = float(input('nota do trabalho de laboratoria: '))
    nota_avaliacao_semestral = float(input('nota da avaliacao semestral: '))
    nota_exame_final = float(input('nota do exame final: '))

    nota_final = (nota_trabalho_laboratoria * 2.0 + nota_avaliacao_semestral * 3.0
                  + nota_exame_final * 5.0) / 3.0

    if 0 <= nota_final <= 2.9:
        print(f'nota final: {nota_final:.2f}')
        print('REPROVADO!')
    elif 3.0 <= nota_final <= 4.9:
        print(f'nota final: {nota_final:.2f}')
        print('RECUPERACAO!')
    else:
        print(f'nota final: {nota_final:.2f}')
        print('APROVADO!')

except ValueError:
    print('O valor informado esta invalido!')
