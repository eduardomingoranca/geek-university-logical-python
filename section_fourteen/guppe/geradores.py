"""
Geradores

- Geradores (Generators) sao Iterators (Iteradores);

OBS: O contrario nao eh verdadeiro. Ou seja, nem todo iterator eh um generator.

Outras informacoes:
- Generators podem ser criados com funcoes geradoras;
- Funcoes geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressoes Geradoras;

Diferencas entre Funcoes e Generator Functions (Funcoes Geradoras)

-----------------------------------------------------------------------------------
| Funcoes                                 | Generator Functions                   |
-----------------------------------------------------------------------------------
| utilizam return                         | utilizam yield                        |
-----------------------------------------------------------------------------------
| retorna uma vez                         | podem utilizar yield multiplas vezes  |
-----------------------------------------------------------------------------------
| quando executada, retorna um valor      | quanto executada, retorna um generator|
-----------------------------------------------------------------------------------


gen = conta_ate(5)

for num in gen:
    print(num)


# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen))  # 1

print('Geek')

for num in gen:
    print(num)

"""

# Exemplo Funcao Geradora (Generator Function)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function nao eh um Generator. Ela gera um generator. ok?


gen = list(conta_ate(10))

print(gen)
