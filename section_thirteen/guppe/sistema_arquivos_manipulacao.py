"""
Sistema de Arquivos - Manipulacao

# Descobrindo se um arquivo ou diretorio existe

# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True


# Diretorio

# Paths relativos
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university'))  # True
print(os.path.exists('geek/university/../geek3.py'))  # False
print(os.path.exists('outro'))  # False

# Paths absolutos
print(os.path.exists('/home/geek/university'))  # False
print(os.path.exists('/home/geek/Imagens'))  # True
print(os.path.exists('/home/geek/Imagens/wallpaler2.png'))  # True

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Criando arquivos

os.mknod('arquivo-teste4.txt')

os.mknod('/home/geek/university.txt')

# OBS: Se voce estiver utilizando no Mac OS, pode javer um erro de PermissionError

# OBS: Criando um arquivo via mknod() se o arquivo ja existir teremos o erro FileExistsError

# Criando diretorios - unicos (um a um)

# Path Relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('/home/geek/templates')

# OBS: A funcao mkdir() cria um diretorio se este nao existir. Caso exista, teremos FileExistsError

os.mkdir('/etc/templates')

# OBS: Se nao tivermos permissao para criar o diretorio teremos um PermissionError

# Criando multi-diretorios (arvore de diretorios)
os.makedirs('templates/geek/university/outro')

# OBS: Se ja existir, teremos um FileExistsError

os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Diretorios
os.rename('geek2/novo2', 'geek2')

# OBS: Se o diretorio nao existir teremos um FileNotFoundError

# OBS: Se e diretorio que queremos renomear nao estiver vazio, teremos um OSError

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')

# Renomear arquivos e diretorios

# Arquivos
os.rename('frutas.txt', 'cesta1.txt')

# ATENcaO! Tome cuidado com os comandos de delecao. Ao deletarmos um arquivo ou diretorio, eles
# nao vao para a lixeira. Eles somem.

# Removendo arquivos
os.remove('geek.txt')

# OBS: Se voce estiver no Windows e o arquivo que voce for deletar estiver em uso, voce tera um erro.

# OBS: Caso o arquivo nao exista, teremos o FileNotFoundError

# OBS: Se voce informar um diretorio ao inves de um arquivo, teremos um IsADirectoryError

# Removendo diretorios vazios

os.rmdir('templates')

# OBS: Se o diretorio tiver qualquer conteudo teremos um OSError

# OBS: Se o diretorio nao existir teremos um FileNotFoundError

# Removendo uma arvore de arquivos
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)


# Podemos remover uma arvore de diretorios vazios

os.removedirs('geek2/mais')

# Se algum dos diretorios contiver arquivos ou outros diretorios, o processo para.

sudo apt-get install lsb-core

os.remove('cesta1.txt')  # Nao vai para a lixeira. Eh deletado imediatamente

# ATENCAO: Ao remover arquivos e diretorios com Python eles nao vao para a lixeira. Eles vao embora!

# Importanto a biblioteca send2trash (Envia arquivos e diretorios para a lixeira)
from send2trash import send2trash

send2trash('cesta2.txt')  # Vai pra lixeira. Pode ser restaurado.

send2trash('teste')

# OBS: Se o arquivo nao existir, teremos OSError

# Trabalhando com arquivos e diretorios temporarios

import os
import tempfile

# Criando um diretorio temporario
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek Univesity\n')
    input()

# Estamos criando um diretorio temporario, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() so para mantermos
# os arquivos temporarios 'vivos' dentro dos blocos with.

# OBS: possivelmente, o codigo acima nao ira funcionar se voce estiver utilizando
# o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos
# temporarios.

# Criando um arquivo temporario

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())


# OBS: Em arquivos temporarios so conseguimos escrever bits. Por isso, utilizamos b''

#Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""
# Trabalhando com arquivos e diretorios temporarios

import os
import tempfile


arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())


input()

arquivo.close()
