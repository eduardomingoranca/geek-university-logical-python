"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrao
w -> Abre para escrita - sobrescreve caso o arquivo ja exista
x -> Abre para escrita somente se o arquivo nao existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteudo ao final do arquivo.
+ -> Abre para o modo de atualizacao: Leitura e Escrita. (Temos o controle do cursor)

#OBS: Abrindo no modo 'a' -> append, se o arquivo nao existir sera criado. Caso exista, o novo conteudo
sera adicionado SEMPRE ao final do arquivo. Com o modo 'a', nao controlamos o cursor.

http://docs.python.org/3/library/functions.html#open

# Exemplo x
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo 2.\n')
except FileExistsError:
    print('Arquivo ja existe')


# Exemplo a
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""

# Exemplo r+
with open('files/outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha.\n')
