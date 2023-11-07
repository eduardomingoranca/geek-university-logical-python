"""
Definindo Funcoes

- Funcoes sao pequenas partes de codigo que realizam tarefas especificas;
- Pode ou nao receber entradas de dados e retornar uma saida de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se voce escrever uma funcao que realiza varias tarefas dentro dela;
eh bom fazer uma verificacao para que a funcao seja simplificada.

Ja utilizamos varias funcoes desde que inicamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;
"""

# Exemplo de utilizacao de funcoes:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a funcao integrada (Built-in) do Python print()

# print(cores)

# curso = 'Programacao em Python: Essencial'

# print(curso)

# cores.append('roxo')

# print(cores)

# curso.append('Mais dados...')  # AttributeError
# print(curso)

# cores.clear()
# print(cores)


# print(help(print))

# DRY - Don't Repeat Yourself - Nao repita voce mesmo / Nao repita seu codigo.

# Mas entao, como definir funcoes?

"""
Em Python, a forma geral de definir uma funcao eh:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao


Onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou nao;
bloco_da_funcao -> Tambem chamado de corpo da funcao ou implementacao, eh onde o processamento da funcao acontece.
Neste bloco, pode ter ou nao retorno da funcao.

OBS: Veja que para definir uma funcao, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma funcao. Tambem abrimos o bloco de codigo com o ja conhecido dois pontos : que eh 
utilizado em Python para definir blocos.
"""

# Definindo a primeira funcao

# Definicao
def diz_oi():
    print('Oi!')

"""
OBS:

1 - Veja que, dentro das nossas funcoes podemos utilizar outras funcoes;
2 - Veja que nossa funcao so executa 1 tarefa, ou seja, a unica coisa que ela faz eh dizer oi;
3 - Veja que esta funcao nao recebe nenhum parâmetro de entrada;
4 - Veja que esta funcao nao retorna nada;
"""

# Utilizando funcoes

# Chamada de execucao
# diz_oi()

"""
ATENCAO:

Nunca esqueca de utilizar o parenteses ao executar uma funcao.

Exemplo:

# Errado!
diz_oi

# Certo
diz_oi()

# Errado
diz_oi ()

"""

# Exemplo 2


def cantar_parabens():
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


#for n in range(5):
#    cantar_parabens()

# Em Python, podemos inclusive criar variaveis do tipo de uma funcao e executar esta funcao atraves da variavel

canta = cantar_parabens

canta()
