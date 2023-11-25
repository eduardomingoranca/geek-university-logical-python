"""
StringIO

ATENCAO: Para ler ou escrever dados em arquivos do sistema operacional o softeware precisa
ter permissao:
    - Permissao de Leitura -> Para ler o arquivo.
    - Permissao de Escrita -> Para escrever o arquivo.


StringIO -> Utilizado para ler e criar arquivos em memoria.
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Este eh apenas uma string normal'

# Podemos criar um arquivo em memoria ja com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que ja sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
