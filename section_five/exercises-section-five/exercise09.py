"""
Leia o salario de um trabalhador e o valor da prestacao de um emprestimo. Se a
prestacao for maior que 20% do salario imprima: Emprestimo nao concedido, caso
contrario imprima: Emprestimo conceito.
"""
try:
    salario_trabalhador = float(input('Informe o salario de um trabalhador - R$ '))
    valor_prestacao_emprestimo = float(input('Informe o valor da prestacao de um emprestimo: '))

    if valor_prestacao_emprestimo > (salario_trabalhador * 0.20):
        print('Emprestimo nao concedido!')
    else:
        print('Emprestimo conceito!')

except ValueError:
    print('O valor informado esta invalido!')
