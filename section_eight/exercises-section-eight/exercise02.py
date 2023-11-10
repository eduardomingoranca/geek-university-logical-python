"""
Faca uma funcao que receba a data atual (dia, mes e ano em inteiro) e exiba-a na tela
no formato textual por extenso.
"""


def data_textual(d, m, a):
    if m == 1:
        return f'{d} de janeiro de {a}'
    elif m == 2:
        return f'{d} de fevereiro de {a}'
    elif m == 3:
        return f'{d} de marco de {a}'
    elif m == 4:
        return f'{d} de abril de {a}'
    elif m == 5:
        return f'{d} de maio de {a}'
    elif m == 6:
        return f'{d} de junho de {a}'
    elif m == 7:
        return f'{d} de julho de {a}'
    elif m == 8:
        return f'{d} de agosto de {a}'
    elif m == 9:
        return f'{d} de setembro de {a}'
    elif m == 10:
        return f'{d} de outubro de {a}'
    elif m == 11:
        return f'{d} de novembro de {a}'
    elif m == 12:
        return f'{d} de dezembro de {a}'


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
