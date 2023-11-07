"""
Funcoes com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')


OBS: Em Python, quando uma funcao nao retorna nenhum valor, o retorno eh None

OBS: Funcoes Python que retornam valores, devem retornar estes valores com a
palavra reservada return

OBS: Nao precisamos necessariamente criar uma variavel para receber o retorno
de uma funcao. Podemos passar a execucao da funcao para outras funcoes.

# Vamos refatorar esta funcao para que ela retorno o valor


def quadrado_de_7():
    return 7 * 7


# Criamos uma variavel para receber o retorno da funcao
ret = quadrado_de_7()
print(f'Ŕetorno {ret}')

print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira funcao

def diz_oi():
    return 'Oi '


alguem = 'Pedro!'

print(diz_oi())
print(alguem)


OBS: Sobre a palavra reservada return

1 - Ela finaliza a funcao, ou seja, ela sai da execucao da funcao;
2 - Podemos ter, em uma funcao, diferentes returns;
3 - Podemos, em uma funcao, retornar qualquer tipo de dado e ate mesmo multiplos valores;

# Exemplos 1 - Ela finaliza a funcao, ou seja, ela sai da execucao da funcao;


def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi! '
    print('Estou sendo executado após o retorno...')


print(diz_oi())

# Exemplo 2 - Podemos ter, em uma funcao, diferentes returns;


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo 3 - Podemos, em uma funcao, retornar qualquer tipo de dado e ate mesmo multiplos valores;


def outra_funcao():
    return 2, 3, 4, 5


#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma funcao para jogar a moeda

from random import random


def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
"""

# Erros comuns na utilizacao do retorno, que na verdade nem eh erro, mas sim codificacao desnecessaria.


def eh_impar():
    numero = 61
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())
