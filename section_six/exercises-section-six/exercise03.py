"""
Faca um algoritmo utilizando o comando while que mostra uma contagem regressiva
na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem 'FIM!' apos a
contagem.
"""
contagem = 10
while contagem >= 0:
    print(contagem)
    if contagem == 0:
        print('FIM!')
        break
    contagem = contagem - 1
