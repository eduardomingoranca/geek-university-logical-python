"""
Dicionarios

OBS: Em algumas linguagens de programacao, os dicionarios Python sao conhecidos
por mapas.

Dicionarios sao colecoes do tipo chave/valor.

Dicionarios sao representados por chaves {}.

print(type({}))

OBS: Sobre dicionarios
    - Chave e valor sao separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


# Criacao de dicionarios

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))


# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que nao existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Remomendada

print(paises.get('br'))
print(paises.get('ru'))


# Caso o get nao encontre o objeto com a chave informada sera retornado o valor None e nao sera gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Nao encontrei o pais')


# Podemos definir um valor padrao para caso nao encontremos o objeto com a chave informada
pais = paises.get('py', 'Nao encontrado')

print(f'Encontrei o pais {pais}')

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusice lista, tupla dicionario, como chaves
# de dicionarios.

# Tuplas por exemplo sao bastante interessantes de serem utilizadas como chave de dicionarios, pois as mesmas
# sao imutaveis.

localidades = {
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em Sao Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSAO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario eh a mesma.
# CONCLUSAO 2: Em dicionarios, NaO podemos ter chaves repetidas.

# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso nao encontre o elemento, um KeyError eh retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto eh sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# Se a chave nao existir sera gerado um KeyError
# OBS: Neste caso o valor removido nao eh retornado.

# Imagine que voce tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preco;
    Produto 2:
        - nome;
        - quantidade;
        - preco;

# 1 - Poderiamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Paystation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual eh o indice de cada informacao no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual eh o indice de cada informacao no produto.

# 3 - Poderiamos utilizar um Dicionario para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informacao.


# Metodos de dicionarios.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)

d.clear()

print(d)

# Copiando um dicionario para outro

# Forma 1 # Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# Forma nao usual de criacao de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))


usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois parametros: um interavel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)
