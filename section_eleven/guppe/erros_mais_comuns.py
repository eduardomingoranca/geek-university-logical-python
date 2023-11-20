"""
Erros mais comuns em Python

ATENCAO! E importante prestar atencao e aprender a ler as saidas de erros geradas pela execucao
do nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, voce escreveu algo que
o Python nao reconhece como parte da linguagem.

Exemplos SyntaxError

a)

def funcao:
    print('Geek University')

b)
 def = 1

c)

return


2 - NameError -> Ocorre quando uma variavel ou funcao nao foi definida.

Exemplos NameError

a)
print(geek)

b)
geek()

3 - TypeError -> Ocorre quando uma funcao/operacao/acao eh aplicada a um tipo errado.

Exemplos TypeError

a)
print(len(5))

b)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um indice invalido.

Exemplos IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

c)
tupla = ('Geek',)
print(tupla[0][10])


5 - ValueError -> Ocorre quando uma funcao/operacao built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado.

Exemplos ValueError

a)
print(int('Geek'))


6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que nao existe.

Exemplos KeyError

a)
dic = {'python': 'university'}
print(dic['geek'])


7 - AttributeError -> Ocorre quando uma variavel nao tem um atributo/funcao.

Exemplos AttributeError

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando nao respeitamos a indentacao do Python (4 espacos)

Exemplos IndentationError

a)
def nova():
print('Geek')

b)

for i in range(10):
i + 1

OBS: Exceptions e Erros sao sinonimos na programacao.

OBS: Importante ler e prestar atencao na saida de erro.
"""
