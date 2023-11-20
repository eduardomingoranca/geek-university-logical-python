"""
Filter

filter() -> Serve para filtrar dados de uma determinada colecao.

# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a funcao mean()
media = statistics.mean(dados)

print(f'Media: {media}')

# OBS: Assim como a funcao map(), a filter() recebe dois parametros, sendo
# uma funcao e um iteravel.

res = filter(lambda valor: valor > media, dados)
print(list(res))

#OBS: Assim como na funcao map(), apos serem utilizados os dados de filter() eles sao excluidos da memoria.

paises = ['', 'Argentina', '', 'Brazil', 'Chile', '', 'Colombia', '', 'Ecuador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

paises = ['', 'Argentina', '', 'Brazil', 'Chile', '', 'Colombia', '', 'Ecuador', '', '', 'Venezuela']

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferenca entre map() e filter() eh:

# map() -> Recebe dois parametros, uma funcao e um iteravel e retorna um objeto mapeando a funcao para cada elemento do
 iteravel.

# filter() -> Recebe dois parametros, uma funcao e um iteravel e retorna um objeto filtrando apenas os elementos de
 acordo com a funcao.

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuarios que estao inativos no Twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Anne', 'Mary']

# Devemos criar uma lista contendo 'Sua instrutrura eh' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora eh {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
