"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separados de casas decimais na programacao eh o ponto e nao a virgula.
"""

# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))


# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# Eh possivel fazer dupla atribuicao
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nos perdemos precisao.
"""
res = int(valor)
print(res)
print(type(res))

#  Podemos trabalhar com numeros complexos
variavel = 5j
