"""
Try / Except / Else / Finally

Dica de quando e onde tratar codigo:

TODA ENTRADA DEVE SER TRATADA!

OBS: A funcao do usuario eh DESTRUIR seu sistema.

# Else -> Eh executado somente se nao ocorrer o erro.

try:
   num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {num}')

# Finally

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Voce nao digitou um valor valido.')
else:
    print(f'Voce digitou o numero {num}')
finally:
    print('Executando o finally')


# OBS: O bloco finally eh SEMPRE executado. Independente se houve excecao ou nao.

# O finally, geralmente, eh utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO


def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro numero: '))

try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo CORRETO
# OBS: Voce eh responsavel pelas entradas das suas funcoes. Entao, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Nao eh possivel realizar uma divisao por zero'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))

# Exemplo mais complexo - Generico
# OBS: Voce eh responsavel pelas entradas das suas funcoes. Entao, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))
"""
# Exemplo mais complexo - Semi-Generico
# OBS: Voce eh responsavel pelas entradas das suas funcoes. Entao, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))
