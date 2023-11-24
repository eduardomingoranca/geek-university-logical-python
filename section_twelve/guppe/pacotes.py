"""
Pacotes

Modulo -> Eh apenas um arquivo Python que pode ter diversas funcoes para utilizarmos;

Pacote -> Eh um diretorio contendo uma colecao de modulos;

OBS: Nas versoes 2.x do Python, um pacote Python deveria conter dentro dele um
arquivo chamado __init__.py

Nas versoes do Python 3.x, nao eh mais obrigatoria a utilizacao deste arquivo, mas
normalmente ainda eh utilizado para manter compatibilidade.

from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())
"""

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4

print(funcao1(6, 9))

print(funcao4())

