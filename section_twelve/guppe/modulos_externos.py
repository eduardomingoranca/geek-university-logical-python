"""
Modulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installler Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> Eh utilizado para permitir impressao de textos coloridos no termimal.

Instalando um modulo:

pip install nome-do-modulo

# Instalando o pacote colorama

pip install colorama

# Utilizando o pacote instalado

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
"""
import pydf
from colorama import init, Fore

pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python:'
                        ' Essencial</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
