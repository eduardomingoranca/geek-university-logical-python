"""
Assertions (Afirmacoes/Checagens/Questionamentos)


Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirmacoes utilizadas nos testes.

Utilizamos o 'assert' em uma expressao que queremos checar se e valida ou nao.
Se a expressao for verdadeira, retorna None eh caso seja falsa levanta um erro
do tipo AssertionError.

# OBS: Nos podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de erro personalizada/

# OBS: A palavra 'assert' pode ser utilizada em qualquer funcao ou codigo nosso....nao precisa
ser exclusivamente nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parametro -O, nenhum assertion
sera validado. Ou seja, todas as suas validacoes ja eram.

"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos numeros precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(2, 4)  # 6
ret = soma_numeros_positivos(-2, 4)  # AssertionError
print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))


# ALERTA: Cuidado ao utilizar 'assert'


def faca_algo_ruim(usuario):
    assert usuario.eh_admin, 'Somente administradores podem fazer coisas ruins!'
    destroi_todo_o_sistema()
    return 'Adeus'
