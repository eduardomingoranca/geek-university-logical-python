"""
Faca uma funcao que receba a data atual (dia, mes e ano em inteiro) e exiba-a na tela
no formato textual por extenso.
"""


def data_textual(dia, mes, ano):
    if mes == 1:
        return f'{dia} de janeiro de {ano}'
    elif mes == 2:
        return f'{dia} de fevereiro de {ano}'
    elif mes == 3:
        return f'{dia} de marco de {ano}'
    elif mes == 4:
        return f'{dia} de abril de {ano}'
    elif mes == 5:
        return f'{dia} de maio de {ano}'
    elif mes == 6:
        return f'{dia} de junho de {ano}'
    elif mes == 7:
        return f'{dia} de julho de {ano}'
    elif mes == 8:
        return f'{dia} de agosto de {ano}'
    elif mes == 9:
        return f'{dia} de setembro de {ano}'
    elif mes == 10:
        return f'{dia} de outubro de {ano}'
    elif mes == 11:
        return f'{dia} de novembro de {ano}'
    elif mes == 12:
        return f'{dia} de dezembro de {ano}'


try:
    loop = True
    while loop:
        dia = int(input('Informe o dia (em inteiro): '))
        mes = int(input('Informe o mes (em inteiro): '))
        ano = int(input('Informe o ano (em inteiro): '))

        if 32 > dia > 0:
            if 0 < mes < 13:
                if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or
                        mes == 8 or mes == 10 or mes == 12):
                    loop = False
                    print(data_textual(dia, mes, ano))
                elif mes == 2:
                    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
                        if dia <= 29:
                            loop = False
                            print(data_textual(dia, mes, ano))
                    else:
                        if dia <= 28:
                            loop = False
                            print(data_textual(dia, mes, ano))
                else:
                    if dia <= 30:
                        loop = False
                        print(data_textual(dia, mes, ano))

except ValueError:
    print('FORMATO INVALIDO!')
