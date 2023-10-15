"""
Determine se um determinado ano lido eh bissexto. Sendo que um ano eh bissexto se
for divisivel por 400 ou se for divisivel por 4 e nao for divisivel por 100. Por
exemplo: 1988, 1992, 1996
"""
try:
    ano = int(input('Informe o ano: '))

    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        print(f'{ano} ano bissexto!')
    else:
        print(f'{ano} ano nao bissexto!')

except ValueError:
    print('O valor informado esta invalido!')
