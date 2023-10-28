"""
Tuplas (tuple)

Tuplas sao bastante parecidas com listas.

Existem basicamente duas diferencas basicas:

1 - As tuplas sao representadas por parenteses ()

2 - As tuplas sao imutaveis: Isso significa que ao se criar uma tupla ela nao muda. Toda
operacao em uma tupla gera uma nova tupla.

# CUIDADO 1: As tuplas sao representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6,)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6,
print(tupla2)

print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso nao eh uma tupla!
print(tupla3)

print(type(tupla3))


tupla4 = (4,)  # Isso eh uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# CONCLUSAO: Podemos concluir que tuplas sao definidas pela virtula e nao pelo uso do parenteses

(4) -> Nao eh tupla
(4,) -> eh tupla
4, -> eh tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programacao em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um numero diferente de elementos para desenpacotar.

# Metodos para adicao e remocao de elementos nas tuplas sao existem, dado o fato das tuplas serem imutaveis.

# Soma*, Valor Maximo*, Valor Minimo* e Tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenacao de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas sao imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)


tupla1 = tupla1 + tupla2  # Tuplas sao imutaveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento esta contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)


for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))


# Dicas na utilizacao de tuplas

# Devemos utilizar tuplas SEMPRE que nao precisarmos modificar os dados contidos em uma colecao

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro'
,'Dezembro')


# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])


# O acesso a elementos de uma tupla tambem eh semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento esta na tupla

print(meses.index('Junho'))

# OBS: Caso o elemento nao exista, sera gerado ValueError.

# Por que utilizar tuplas?

# - Tuplas sao mais rapidas do que listas.
# - Tuplas deixam seu codigo mais seguro*.

# * Isso porque trabalhar com elementos imutaveis traz seguranca para o codigo.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla nao temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)

"""