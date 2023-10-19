"""
Leia uma data e determine se ela eh valida. Ou seja, verifique se o mes esta 1 e 12,
e se o dia existe naquele mes. Note que Fevereiro tem 29 dias em anos bissextos, e 28
dias em anos nao bissextos.
"""
try:
    data = input('Informe uma data valida (dd/mm/aaaa): ')

    x = data.split('/')
    dia = int(x.__getitem__(0))
    mes = int(x.__getitem__(1))
    ano = int(x.__getitem__(2))

    DATA_INVALIDA = "DATA INVALIDA!"

    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
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

except ValueError:
    print('O formado do dado informado esta invalido!')
