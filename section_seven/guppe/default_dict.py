"""
Modulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionarios

dicionario = {'curso': 'Programacao em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro'])  # ??? KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nos informamos um valor default,
podendo utilizar um lambda para isso. Este valor sera utilizado sempre que nao houver
um valor definido. Caso tentemos acessar uma chave que nao existe, essa chave sera
criada e o valor default sera attribuido.

OBS: Lambdas sao funcoes sem nome, que podem ou nao receber parametros de entrada
e retornar valores.
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programacao em Python: Essencial'

print(dicionario)

print(dicionario['outro'])  # KeyError no dicionario comum, mas aqui nao.

print(dicionario)
