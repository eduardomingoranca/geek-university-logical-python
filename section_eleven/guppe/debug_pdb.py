"""
Debuggando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# OBS: A utilizacao do print() para debugar codigo eh uma pratica ruim.

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger

# Exemplo com o PyCharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 0))

# Exemplo com o PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e entao utilizar a funcao set_trace()

# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo com o PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e entao utilizar a funcao set_trace()

# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O debug eh utilizado durante o desenvolvimento. Custumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao inves de colocarmos o import do pdb no inicio do arquivo,
# nos colocamos somente onde vamos debuggar, e ao finalizar ja fazemos a remocao.

# Exemplo com o PDB - Python Debugger - Exemplo 3

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e entao utilizar a funcao set_trace()

# * A partir do Python 3.7, nao eh mais necessario importar a biblioteca pdb, pois o comando de debug foi
# incorporado como funcao built-in (integrada) chamada breakpoint()

# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variaveis e os comandos do pdb
"""


def soma(k, n, p, c):
    breakpoint()
    return k + n + p + c


print(soma(1, 3, 5, 7))

# Como os nomes das variaveis sao os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variaveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes nao representativos em variaveis. Sempre optar por nomes significativos.


def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
