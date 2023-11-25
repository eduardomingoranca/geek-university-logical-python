"""
Leitura de Arquivos

Para o conteudo de um arquivo em Python, utilizamos a funcao integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilizacao nos passamos apenas um parametro
de entrada, que neste caso eh o caminho para o arquivo a ser lido. Essa funcao retorna
um _io.TextIOWrapper e eh com ele que trabalhamos entao.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrao, a funcao open() abre o arquivo para leitura. Este arquivo
deve existir, ou entao teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

mode r -> Modo de Leitura. r -> read() -> ler

"""

# Exemplo

arquivo = open('texto.txt')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteudo de um arquivo, apos sua abertura, devemos utilizar a funcao read()

ret = arquivo.read()

print(type(ret))

print(ret)

# print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# print(arquivo.read())

# OBS: A funcao read() le todo o conteudo do arquivo.
