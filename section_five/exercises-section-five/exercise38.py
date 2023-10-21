"""
Leia uma data de nascimento de uma pessoa fornecida atraves de tres numeros inteiros:
Dia, Mes e Ano. Teste a validade desta data para saber se esta eh uma data valida. Teste
se o dia fornecido eh um dia valido: dia > 0, dia < 28 para o mes de fevereiro (29 se o
ano for bissexto), dia <= 30 em abril, junho, setembro e novembro, dia <= 31 no outros
meses. Teste a validade do mes: mes > 0 e mes < 13. Teste a validade do ano: ano <= ano
atual (use uma constante definida com o valor igual a 2023). Imprimir: 'data valida'
ou 'data invalida' no final da execucao do programa.
"""
try:
    data = input('Informe uma data valida (dd/mm/aaaa): ')

    x = data.split('/')
    dia = int(x.__getitem__(0))
    mes = int(x.__getitem__(1))
    ano = int(x.__getitem__(2))

    ANO_ATUAL = 2023
    DATA_INVALIDA = "DATA INVALIDA!"

    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1 or ano > ANO_ATUAL:
        print(DATA_INVALIDA)
    elif mes == 2:
        if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
            if dia > 29:
                print(DATA_INVALIDA)
        else:
            if dia > 28:
                print(DATA_INVALIDA)
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            print(DATA_INVALIDA)
    else:
        print('DATA VALIDA!')

except ValueError:
    print('O formado do dado informado esta invalido!')
