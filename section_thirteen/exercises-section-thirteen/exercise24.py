"""
Implemente um controle simples de mercadorias em uma despensa domestica. Para
cada produto armazene um codigo numerico, descricao e quantidade atual. O programa
deve ter opcoes para entrada e retirada de produtos, bem como um relatorio geral e
um de produtos nao disponiveis. Armazene os dados em arquivo binario.
"""

with open('files/report.txt', 'w') as file:
    while True:
        codigo = int(input('Informe o codigo inteiro do produto: '))
        descricao = input('Informe uma descricao do produto: ')
        quantidade = int(input(f'Informe a quantidade atual de {descricao}: '))
        if codigo >= 0 and quantidade >= 0:
            file.write(str(codigo) + ' ' + descricao + ' ' + str(quantidade))
            file.write('\n')
        else:
            break

print(open('files/report.txt').read())
