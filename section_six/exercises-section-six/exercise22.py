"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequencia arbitraria de notas (validas no intervalo de 10 a 20) e que mostre na tela,
como resultado, a correspondente media aritmetica. O numero de notas com que o aluno
pretenda efetuar o calculo nao sera fornecido ao programa, o qual terminara quando for
introduzido um valor que nao seja valido como nota de aprovacao.
"""
try:
    loop = True
    soma = 0
    quantidade = 0
    while loop:
        nota = float(input('Informe a nota: '))

        if 10 <= nota <= 20:
            soma = soma + nota
            quantidade = quantidade + 1
        else:
            loop = False
            print(f'A MEDIA DAS NOTAS: {soma / quantidade}')

except ValueError:
    print('O formato de valor informado esta invalido!')
