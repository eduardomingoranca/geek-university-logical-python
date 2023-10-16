"""
Faca uma prova de matematica para criancas que estao aprendendo a somar numeros
inteiros menores do que 100. Escolha numeros aleatorios entre 1 e 100, e mostre
na tela a pergunta: qual eh a soma de a + b, onde a e b sao os numeros aleatorios.
Peca a resposta. Faca cinco perguntas ao aluno, e mostre para ele as perguntas e
as respostas corretas, alem de quantas vezes o aluno acertou.
"""
from random import randint

try:
    loop = 1
    acerto = 0
    erro = 0
    while loop < 6:
        a = randint(1, 100)
        b = randint(1, 100)
        resposta = int(input(f'Qual eh a soma de {a} + {b}: '))
        soma = a + b

        if resposta == soma:
            acerto = acerto + 1
        else:
            erro = erro + 1

        loop = loop + 1

    print(f'ACERTOS: {acerto} | ERROS: {erro}')
except ValueError:
    print('O valor informado esta invalido!')
