"""
Trabalhando com Modulos Builtin (modulos integrados, que ja vem instalados no Python)
________________________
|Python|Modulos builtin|
------------------------

# Utilizando alias (apelidos) para modulos/funcoes
import random as rdm


print(rdm.random())

# Podemos importar todas as funcoes de um modulo utilizando o *

from random import *


print(random())

# Importando todo o modulo

import random


print(random.random())

# Utilizando alias (apelidos) para modulos/funcoes

from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelidos) para modulos/funcoes

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())


https://docs.python.org/3/py-modindex.html

"""
# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo modulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))
