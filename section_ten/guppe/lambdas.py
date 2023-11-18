"""
Utilizando Lambdas

Conhecidas por Expressoes Lambdas, ou simplesmente Lambdas, sao funcoes sem nome, ou seja,
funcoes anonimas.

# Funcao em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressao Lambda
lambda x: 3 * x + 1

# E como utilizar a expressao lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressoes lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo('  FELICITY       ', ' jones '))

# Em funcoes Python podemos ter nenhuma ou varias entradas. Em Lambdas tambem

amar = lambda: 'Como nao amar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressao>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#OBS: Se passarmos mais argumentos do que parametros esperados teremos TypeError

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""


# Funcao Quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a funcao

def geradora_funcao_quadratica(a, b, c):
    """Retorna a funcao f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)


print(teste(0))
print(teste(1))
print(teste(2))


print(geradora_funcao_quadratica(3, 0, 1)(2))
