"""
Preservando metadatas com wraps

Metadados -> Sao dados intrisecos em arquivos.

wraps -> Sao funcoes que envolvem elementos com diversas finalizades.

# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma funcao (logar) dentro de outra
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    # Soma dois numeros.
    return a + b


# print(soma(10, 30))

print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois numeros.


"""


# Resolucao do Problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma funcao (logar) dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Aqui a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros."""
    return a + b


# print(soma(10, 30))

print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois numeros.

print(help(soma))
