"""
Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se
aposentar. As condicoes para aposentadoria sao
    <> Ter pelo menos 65 anos;
    <> Ou ter trabalhado pelo menos 30 anos;
    <> Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos;
"""
try:
    idade = int(input('Informe a idade: '))
    tempo_servico = int(input('Informe o tempo de servico (em anos): '))

    if idade >= 65 or tempo_servico >= 30 or idade >= 60 and tempo_servico >= 25:
        print('PODE APOSENTAR!')
    else:
        print('NAO PODE APOSENTAR!')

except ValueError:
    print('O valor informado esta invalido!')
