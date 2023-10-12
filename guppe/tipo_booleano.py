"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False - Falso

OBS: Sempre com a inicial mainúscula

Errado:

true, false

Certo:

True, False
"""

ativo = False

print(ativo)

"""
Operacões basicas:
"""

#  Negacao (not):
"""
Fazendo a negacao, se o valor booleano for verdadiro o resultado sera falso,
se for falso o resultado sera verdadeiro. Ou seja, sempre o contrario.
"""
print(not ativo)

logado = False

#  Ou (or):
"""
Eh uma operacao binaria, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

#  E (and):
"""
Tambem eh uma operacao binaria, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""