"""
Sistema de Arquivos e Navegacao

Para fazer uso de manipulacao de arquivos do sistema operacional, precisamos importar
e fazer uso do modulo os.

os -> Operating System - Sistema Operacional


# getcwd() -> pega o current work directory - diretorio de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())  # /media/sf_Documents/vm/PyCharmProjects/guppe

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())  # /media/sf_Documents/vm/PyCharmProjects


os.chdir('..')

print(os.getcwd())  # /media/sf_Documents/vm


os.chdir('..')

print(os.getcwd())  # /media/sf_Documents

os.chdir('..')

print(os.getcwd())  # /media


os.chdir('..')

print(os.getcwd())  # /


os.chdir('..')

print(os.getcwd())  # /

# Podemos checar se um diretorio eh absoluto ou relativo

print(os.path.isabs('/home/geek/'))  # True

# OBS para usuarios Windows
# Se voce, infelizmente, estiver utilizando um computador com Windows,
# tera que ter cuidado ao verificar diretorios.

print(os.path.isabs('C:\\Users\\geek'))

# Podemos identificar o sistema operacional com o modulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

# Fazer o import
import sys

print(sys.platform)

# '/home/geek/workspace/sistema'

print(os.getcwd())  # /media/sf_Documents/vm/PycharmProjects/guppe

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())  # /media/sf_Documents/vm/PycharmProjects/guppe/geek/university

# Veja que o os.path.join() recebe dois parametros, sendo o primeiro o diretorio atual e o segundo o
# diretorio que sera juntado ao atual.

# Podemos listar os arquivos e diretorios com o listdir()

print(os.listdir('/etc'))
"""

import os

# Podemos listar os arquivos e diretorios com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(scanner)

# print(arquivos)

# print(dir(arquivos[0]))


print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # Eh um diretorio? False
print(arquivos[0].is_file())  # Eh um arquivo? True
print(arquivos[0].is_symlink())  # Eh um link simbolico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho ate o arquivo
print(arquivos[0].stat())  # Estatisticas...

# OBS: Quando utilizamos a funcao scandir() nos precisamos fecha-la, assim quando abrimos um arquivo.

scanner.close()
