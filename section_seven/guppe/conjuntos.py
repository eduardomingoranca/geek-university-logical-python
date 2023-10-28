"""
Conjuntos

- Conjuntos em qualquer linguagem de programacao, estamos fazendo referencia a Teoria dos Conjuntos
da Matematica.

- Aqui no Python, os conjuntos sao chamados de Sets.

Dito isto, da mesma forma que na matematica:

- Sets (conjuntos) nao possuem valores duplicados;
- Sets (conjuntos) nao possuem valores ordenados;
- Elementos nao sao acessados via indice, ou seja, conjuntos nao sao indexados;

Conjuntos sao bons para se utilizar quando precisamos armazenar elementos
mas nao nos importamos com a ordenacao deles. Quando nao precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) sao referenciados em Python com chaves {}

Diferenca entre Conjuntos (Set) e Mapas (Dicionarios) em Python:
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5,  6, 7, 2, 3})  # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo
# sera ignorado sem gerar error e nao fara parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Importante lembrar que, alem de nao termos valores dupliados, nao temos ordem

# Listas aceitam valores duplicados, entao temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, entao temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla}  com {len(tupla)} elementos')

# Dicionarios nao aceitam chaves duplicadas, entao temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario}  com {len(dicionario)} elementos')

# Conjuntos nao aceitam valores duplicados, entao temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto}  com {len(conjunto)} elementos')


# Assim como todo outro conjunto Python podemos colocar tipos de daods misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, ja que em uma lista podemos adicionar novos elementos
# e ter repeticao.

cidades = ['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos.

# O que voce faria? Faria um llop na lista....?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade nao gera erro. Simplesmente eh ignorado e nao eh adicionado.
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  #  Nao eh indice! Informamos o valor a ser removido.

print(s)

# OBS: Caso o valor nao seja encontrado sera gerado o erro KeyError. Nenhum valor eh retornado.

# Forma 2

s.discard(22)

print(s)

# OBS: Se o valor nao for encontrado, nenhum erro eh gerado.

# Copiando um conjunto para outro...

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}


# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
# {'Pedro', 'Fernando', 'Ana', 'Julia', 'Guilherme', 'Patricia', 'Marcos', 'Ellen', 'Gustavo'}
# unicos1 = estudantes_java.union(estudantes_python)
# {'Ana', 'Marcos', 'Gustavo', 'Fernando', 'Patricia', 'Guilherme', 'Pedro', 'Ellen', 'Julia'}
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Veja que alguns alunos que estudam Python tambem estudam Java.

# Gerar um conjunto de estudantes que estao am ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Metodos Matematicos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

# Gerar um conjunto de estudantes que nao estao no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
