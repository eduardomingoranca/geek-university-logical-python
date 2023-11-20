"""
Generator Expression

Em aulas anteriores nos estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Nao vimos:
- Tuple Comprehension....porque elas se chamam Generators

nomes = ['Charles', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])

# Poderiamos ter feito utilizando Generators

nomes = ['Charles', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual eh a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memoria do elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' esta ocupando em memoria. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))

from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')
"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
