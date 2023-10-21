"""
Uma empresa decide dar um aumento aos seus funcionarios de acordo com uma tabela
que considera o salario atual e o tempo de servico de cada funcionario. Os funcionarios
com menor salario terao um aumento proporcionalmente maior do que os funcionarios
com um salario maior, e conforme o tempo de servico na empresa, cada funcionario ira
receber um bonus adicional de salario. Faca um programa que leia:

        <> o valor do salario atual do funcionario;
        <> o tempo de servico desse funcionario na empresa (numero de anos de trabalho na
        empresa).

Use as tabelas abaixo para calcular o salario reajustado deste funcionario e imprima o
valor do salario final reajustado, ou uma mensagem caso o funcionario nao tenha direito
a nenhum aumento.

        | Salario Atual    | Reajuste (%) | Tempo de Servico | Bonus     |
        | Ate 500.00       |    25%       | Abaixo de 1 ano  | Sem bonus |
        | Ate 1000.00      |    20%       | De 1 a 3 anos    | 100.00    |
        | Ate 1500.00      |    15%       | De 4 a 6 anos    | 200.00    |
        | Ate 2000.00      |    10%       | De 7 a 10 anos   | 300.00    |
        | Acima de 2000.00 | Sem reajuste | Mais de 10 anos  | 500.00    |

"""
try:
    valor_salario = float(input('Informe o valor do salario atual do funcionario - R$ '))
    tempo_servico = int(input('Informe o tempo de servico desse funcionario na empresa (em anos): '))

    if valor_salario <= 500.00:
        salario_reajustado = valor_salario * 1.25
        if tempo_servico < 1:
            print(f'Salario Reajustado R$ {salario_reajustado} - Sem bonus')
        elif 1 <= tempo_servico <= 3:
            print(f'Salario Reajustado R$ {salario_reajustado + 100.00} - Bonus de R$ 100.00')
        elif 4 <= tempo_servico <= 6:
            print(f'Salario Reajustado R$ {salario_reajustado + 200.00} - Bonus de R$ 200.00')
        elif 7 <= tempo_servico <= 10:
            print(f'Salario Reajustado R$ {salario_reajustado + 300.00} - Bonus de R$ 300.00')
        else:
            print(f'Salario Reajustado R$ {salario_reajustado + 500.00} - Bonus de R$ 500.00')
    elif valor_salario <= 1000.00:
        salario_reajustado = valor_salario * 1.20
        if tempo_servico < 1:
            print(f'Salario Reajustado R$ {salario_reajustado} - Sem bonus')
        elif 1 <= tempo_servico <= 3:
            print(f'Salario Reajustado R$ {salario_reajustado + 100.00} - Bonus de R$ 100.00')
        elif 4 <= tempo_servico <= 6:
            print(f'Salario Reajustado R$ {salario_reajustado + 200.00} - Bonus de R$ 200.00')
        elif 7 <= tempo_servico <= 10:
            print(f'Salario Reajustado R$ {salario_reajustado + 300.00} - Bonus de R$ 300.00')
        else:
            print(f'Salario Reajustado R$ {salario_reajustado + 500.00} - Bonus de R$ 500.00')
    elif valor_salario <= 1500.00:
        salario_reajustado = valor_salario * 1.15
        if tempo_servico < 1:
            print(f'Salario Reajustado R$ {salario_reajustado} - Sem bonus')
        elif 1 <= tempo_servico <= 3:
            print(f'Salario Reajustado R$ {salario_reajustado + 100.00} - Bonus de R$ 100.00')
        elif 4 <= tempo_servico <= 6:
            print(f'Salario Reajustado R$ {salario_reajustado + 200.00} - Bonus de R$ 200.00')
        elif 7 <= tempo_servico <= 10:
            print(f'Salario Reajustado R$ {salario_reajustado + 300.00} - Bonus de R$ 300.00')
        else:
            print(f'Salario Reajustado R$ {salario_reajustado + 500.00} - Bonus de R$ 500.00')
    elif valor_salario <= 2000.00:
        salario_reajustado = valor_salario * 1.10
        if tempo_servico < 1:
            print(f'Salario Reajustado R$ {salario_reajustado} - Sem bonus')
        elif 1 <= tempo_servico <= 3:
            print(f'Salario Reajustado R$ {salario_reajustado + 100.00} - Bonus de R$ 100.00')
        elif 4 <= tempo_servico <= 6:
            print(f'Salario Reajustado R$ {salario_reajustado + 200.00} - Bonus de R$ 200.00')
        elif 7 <= tempo_servico <= 10:
            print(f'Salario Reajustado R$ {salario_reajustado + 300.00} - Bonus de R$ 300.00')
        else:
            print(f'Salario Reajustado R$ {salario_reajustado + 500.00} - Bonus de R$ 500.00')
    else:
        if tempo_servico < 1:
            print(f'Sem reajuste salario e Sem bonus - R$ {valor_salario}')
        elif 1 <= tempo_servico <= 3:
            print(f'Sem reajuste salario e com bonus de R$ 100.00 - R$ {valor_salario + 100.00}')
        elif 4 <= tempo_servico <= 6:
            print(f'Sem reajuste salario e com bonus de R$ 200.00 - R$ {valor_salario + 200.00}')
        elif 7 <= tempo_servico <= 10:
            print(f'Sem reajuste salario e com bonus de R$ 300.00 - R$ {valor_salario + 300.00}')
        else:
            print(f'Sem reajuste salario e com bonus de R$ 500.00 - R$ {valor_salario + 500.00}')

except ValueError:
    print('O formado do dado informado esta invalido!')
