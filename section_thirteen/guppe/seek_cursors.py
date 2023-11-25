"""
Seek e Cursors

seek() -> Eh utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())


# seek() -> A funcao seek() eh utilizada para  movimentacao do cursor pelo arquivo. Ela recebe um
# parametro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a funcao seek() -> Procurar
arquivo.seek(0)


print(arquivo.read())


arquivo.seek(22)

print(arquivo.read())

# readline() -> Funcao que le o arquivo linha a linha (readline -> le linha)

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a funcao open() eh criada uma conexao entre o arquivo
no disco do computador e o nosso programa. Essa conexao eh chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexao. Para isso utilizamos a funcao close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed)  # False Verifica se o arquivo esta aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()


print(arquivo.closed)  # True - Verifica se o arquivo esta aberto ou fechado


print(arquivo.read())

# OBS: Se tentarmos manipular o arquivo apos seu fechamento, teremos um ValueError
"""

arquivo = open('files/texto.txt')

# Com a funcao read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))
