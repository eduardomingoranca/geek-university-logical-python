"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o metodo
# writerow() para escrever cada linha. Este metodo recebe uma lista.

from csv import writer


with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracao (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

"""


# DictWriter

# OBS: As chaves do dicionario devem ser as mesmas utilizadas como cabecalho.

from csv import DictWriter


with open('files/csv/filmes3.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracao (em minutos): ')
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})
