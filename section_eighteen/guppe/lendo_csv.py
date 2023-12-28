"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Virgula

# Separador por virula

1, 2, 3, 4, 5, 6

"geek", "university", "python", 'ciencia", "dados"

# Separador por ponto eh virgula

1; 2; 3; 4; 5; 6

"geek"; "university"; "python"; 'ciencia"; "dados"

# Separador por espaco

1 2 3 4 5 6

"geek" "university" "python" 'ciencia" "dados"

http://dados.gov.br/dataset

# Possivel de se trabalhar, mas naoeo ideal (trabalhoso)

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)


A linguagem Python possui duas formas diferente para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader

from csv import reader


with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabecalho
    for linha in leitor_csv:
        # Cada linhaeuma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} eh mede {linha[2]} centimetros')


# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linhaeum OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['Pais']} eh mede {linha['Altura (em cm)']}")
"""

# DictReader com outro separador

from csv import DictReader

with open('files/csv/lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linhaeum OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['Pais']} eh mede {linha['Altura (em cm)']}")
