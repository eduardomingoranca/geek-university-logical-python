"""
Teste de Memoria com Generators


# Sequencia de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 Lista
for n in fib_lista(100000):
    print(n)

"""

# Funcao usando listas 449MB


def fib_lista(maximum):
    nums = []
    a, b = 0, 1
    while len(nums) < maximum:
        nums.append(b)
        a, b = b, a + b
    return nums


# Funcao usando geradores

def fib_gen(maxi):
    a, b, contador = 0, 1, 0
    while contador < maxi:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 Geradores 3MB
for n in fib_gen(100000):
    print(n)
