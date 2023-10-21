"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range par trabalhar melhor com loops for.

Ranges sao utilizados para gerar sequencias numericas, nao de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada nao inclusive (inicio padrao 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada nao inclusive (inicio especificado pelo usuario, e passo de 1 em 1)

# Exemplo Forma 2
for num in range(4, 11):
    print(num)


# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada nao inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo Forma 3
for num in range(5, 55, 5):
    print(num)

Forma 4 (Inversa)

range(valor_de_incio, valor_de_parada, passo)

OBS: valor_de_parada nao inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo Forma 4
for num in range(10, -1, -1):
    print(num)
"""