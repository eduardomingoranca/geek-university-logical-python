"""
Escrevendo em arquivos


# OBS: Ao abrir um arquivo para leitura, nao podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, nao podemos le-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo eh criado no sistema operacional.

Para escrevermos dados em um arquivo, apos abrir o arquivo utilizamos a funcao write().
Esta funcao recebe uma string como parametro, caso contrario teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo nao existir sera criado,
caso ele ja exista, o anterior sera apagado e um novo sera criado. Dessa forma, todo
o conteudo no arquivo anterior eh perdido.

# Exemplo de escrita - modo 'w' - write (escrita)


# Forma tradicional de escrita em arquivo (Nao Pythonica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()


# Forma Pythonica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Mais Esta eh a ultima linha.')


with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
"""
with open('files/frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
