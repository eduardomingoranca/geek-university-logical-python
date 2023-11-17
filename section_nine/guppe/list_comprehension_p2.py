"""
List Comprehension

Nos podemos adicionar estruturas condicionais logicas as nossas List Comprehension
"""

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar

# Qualquer numero par modulo de 2 eh 0 e 0 em Python eh False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer numero impar modulo de 2 eh 1, e 1 em Python eh True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
