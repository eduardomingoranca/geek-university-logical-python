"""
Modulo Random e o que sao modulos?

- Em Python, modulos nada mais sao do que outros arquivos Python.

Modulo Random -> Possui varias funcoes para geracao de numeros pseudo-aleatorio.

# OBS: Existem duas formas de se utilizar um modulo ou funcao deste

# Forma 1  - Importando todo o modulo (Nao recomendado).

import random

# random() -> Gera um numero real pseudo-aleatorio entre 0 e 1.

# OBS: Ao realizar o import de todo o modulo, todas as funcoes, atributos, classes e propriedades que estiverem
# dentro do modulo ficarao disponiveis (Ficarao em Memoria). Caso voce saiba quais funcoes voce precisa utilizar
# deste modulo, entao esta nao seria a forma ideal de utilizacao. Nos veremos uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a funcao random() do pacote random, nos colocamos o nome do pacote e o nome da funcao,
# seprados por ponto.

# OBS: Nao confunda a funcao random() com o pacote random. Pode parecer confuso, mas a funcao random() eh
# apenas uma funcao dentro do modulo random.

# Forma 2 - Importando uma funcao especifica do modulo (Forma recomendada)

from random import random

# No import acima, estamos falando: Do modulo random, importe a funcao random

for i in range(10):
    print(random())

# uniform() -> Gerar um numero real pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10))  # 10 nao eh incluido.


# randint() -> Gera valores inteiros pseudo-aleatorios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # comeca em 1 e vai ate 60

# choice() -> Mostra um valor aleatorio entre um iteravel.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
"""

from random import shuffle

# shuffle() -> Tem a funcao de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())
