"""
Loop while

Forma geral

while expressao_booleana:
    //execucao do loop


O bloco do while sera repetido enquanto a expressao booleana for verdadeira.

Expressao Booleada eh toda expressao onde o resultado eh verdadeiro ou falso.

Exemplo:

num = 5

num < 5


# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    # numero = numero + 1

# OBS: Em um loop while, eh importante que cuidemos do criterio de parada para nao causar um loop infinito.

# C ou Java

while(expressao) {
  //execucao
}

# do while (C ou Java)

do {
    //execucao
} while(expressao);

"""

# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Ja acabou? ')
