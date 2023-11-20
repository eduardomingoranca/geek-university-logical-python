"""
Modulos Customizados

Como modulos Python nada mais sao do que arquivos Python, entao TODOS os arquivos que criamos
neste curso sao modulos Python prontos para serem utilizados.

# Importando uma funçao especifica do nosso modulo
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Importando todo o modulo (Temos acesso a TODOS os elementos do modulo)
import funcoes_com_parametro as fcp


# Estamos acessando e imprimindo uma variavel contida no modulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
