"""
A importancia de R$ 780.000,00 sera dividida entre tres ganhadores de um concurso.
Sendo que da quantia total:
    . O primeiro ganhador recebera 46%
    . O segundo recebera 32%
    . O terceiro recebera o restante
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
print(f'PREMIO DE R$ {780000}')
print(f'1ª ganhador: R$ {780000 * 0.46}')
print(f'2º ganhador: R$ {780000 * 0.32}')
print(f'3º ganhador: R$ {780000 - ((780000 * 0.32) + (780000 * 0.46))}')
