"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo. Previnindo
assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples eh:

try:
    //execucao problematica
except:
    //o que deve ser feito em caso de problema


# Exemplo 1 - Tratando um erro generico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a funcao geek(), caso voce encontre erros, imprima a mensagem de erro.


# Exemplo 2 - Tratando um erro generico

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a funcao geek(), caso voce encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma generica nao eh a melhor forma de tratamento de erros. O ideal eh SEMPRE
tratar de forma especifica.

# Exemplo 3 - Tratando um erro especifico

try:
    geek()
except NameError:
    print('Voce esta utilizando uma funcao inexistente')


# Exemplo 4 - Tratando um erro especifico

try:
    len(5)
except TypeError:
    print('Voce esta utilizando uma funcao inexistente')

# Exemplo 5 - Tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicacao gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    geek()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}

print(pega_valor(dic, 8))
