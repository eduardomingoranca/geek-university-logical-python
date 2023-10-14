"""
Tres amigos jogaram na loteria. Caso eles ganhem, o premio deve ser repartido proporcionalmente
ao valor que cada deu para a realizacao da aposta. Faca um programa que leia quanto cada apostador
investiu, o valor do premio, e imprima quanto cada um ganharia do premio com base no valor investido.
"""
try:
    apostador_um = float(input('Informe o valor do 1º apostador - R$ '))
    apostador_dois = float(input('Informe o valor do 2º apostador - R$ '))
    apostador_tres = float(input('Informe o valor do 3º apostador - R$ '))

    premio = float(input('Informe o valor do premio - R$ '))

    if apostador_um > apostador_dois > apostador_tres:
        soma = apostador_um + apostador_dois + apostador_tres
        premio_apostador_um = premio / (soma / apostador_um)
        premio_apostador_dois = premio / (soma / apostador_dois)
        premio_apostador_tres = premio / (soma / apostador_tres)
        print(f'VALOR PREMIO - R$ {premio}')
        print(f'VALOR 1º APOSTADOR - R$ {premio_apostador_um:.2f}')
        print(f'VALOR 2º APOSTADOR - R$ {premio_apostador_dois:.2f}')
        print(f'VALOR 3º APOSTADOR - R$ {premio_apostador_tres:.2f}')
    elif apostador_um > apostador_tres > apostador_dois:
        soma = apostador_um + apostador_dois + apostador_tres
        premio_apostador_um = premio / (soma / apostador_um)
        premio_apostador_dois = premio / (soma / apostador_dois)
        premio_apostador_tres = premio / (soma / apostador_tres)
        print(f'VALOR PREMIO - R$ {premio}')
        print(f'VALOR 1º APOSTADOR - R$ {premio_apostador_um:.2f}')
        print(f'VALOR 3º APOSTADOR - R$ {premio_apostador_tres:.2f}')
        print(f'VALOR 2º APOSTADOR - R$ {premio_apostador_dois:.2f}')
    elif apostador_dois > apostador_tres > apostador_um:
        soma = apostador_um + apostador_dois + apostador_tres
        premio_apostador_um = premio / (soma / apostador_um)
        premio_apostador_dois = premio / (soma / apostador_dois)
        premio_apostador_tres = premio / (soma / apostador_tres)
        print(f'VALOR PREMIO - R$ {premio}')
        print(f'VALOR 2º APOSTADOR - R$ {premio_apostador_dois:.2f}')
        print(f'VALOR 3º APOSTADOR - R$ {premio_apostador_tres:.2f}')
        print(f'VALOR 1º APOSTADOR - R$ {premio_apostador_um:.2f}')
    elif apostador_dois > apostador_um > apostador_tres:
        soma = apostador_um + apostador_dois + apostador_tres
        premio_apostador_um = premio / (soma / apostador_um)
        premio_apostador_dois = premio / (soma / apostador_dois)
        premio_apostador_tres = premio / (soma / apostador_tres)
        print(f'VALOR PREMIO - R$ {premio}')
        print(f'VALOR 2º APOSTADOR - R$ {premio_apostador_dois:.2f}')
        print(f'VALOR 1º APOSTADOR - R$ {premio_apostador_um:.2f}')
        print(f'VALOR 3º APOSTADOR - R$ {premio_apostador_tres:.2f}')
    elif apostador_tres > apostador_dois > apostador_um:
        soma = apostador_um + apostador_dois + apostador_tres
        premio_apostador_um = premio / (soma / apostador_um)
        premio_apostador_dois = premio / (soma / apostador_dois)
        premio_apostador_tres = premio / (soma / apostador_tres)
        print(f'VALOR PREMIO - R$ {premio}')
        print(f'VALOR 3º APOSTADOR - R$ {premio_apostador_tres:.2f}')
        print(f'VALOR 2º APOSTADOR - R$ {premio_apostador_dois:.2f}')
        print(f'VALOR 1º APOSTADOR - R$ {premio_apostador_um:.2f}')
    else:
        soma = apostador_um + apostador_dois + apostador_tres
        premio_apostador_um = premio / (soma / apostador_um)
        premio_apostador_dois = premio / (soma / apostador_dois)
        premio_apostador_tres = premio / (soma / apostador_tres)
        print(f'VALOR PREMIO - R$ {premio}')
        print(f'VALOR 3º APOSTADOR - R$ {premio_apostador_tres:.2f}')
        print(f'VALOR 1º APOSTADOR - R$ {premio_apostador_um:.2f}')
        print(f'VALOR 2º APOSTADOR - R$ {premio_apostador_dois:.2f}')

except ValueError:
    print('O valor informado esta invalido!')
