"""
Levantando os proprios erros com raise

raise -> Lanca excecoes

OBS: O raise nao eh uma funcao. Eh uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas proprias excecoes e mensagens
de erro.

A forma geral de utilizacao eh:

raise TipoDoErro('Mensagem de erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('True', 7)


# Exemplo refatorado


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')

OBS: O raise, assim como o return, finaliza a funcao. Ou seja, nada apos o raise eh executado.

"""

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')
