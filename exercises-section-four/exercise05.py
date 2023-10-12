"""
Leia um numero real e imprima a quinta parte deste numero
"""
try:
    numero = float(input('Informe um numero real: '))
    quinta_parte = numero / 5
    print(f'A quinta parte do numero {numero} eh {quinta_parte}')
except ValueError:
    print('O valor informado eh invalido!')
