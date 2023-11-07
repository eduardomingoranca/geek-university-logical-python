"""
Funcoes com Parametro (de entrada)

- Funcoes que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

Se a gente pensar em uma funcao, ja sabemos que temos funcoes que:
- Nao possuem entrada;
- Nao possuem saida;
- Possuem entrada mas nao possuem saida;
- Nao possuem entrada mas possuem saida;
- Possuem entrada e saida;

# Refatorando uma funcao


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado())  # TypeError

# Refatorando a funcao


def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')


cantar_parabens('Patricia')

# Funcoes podem ter n parametros de entada. Ou seja, podemos receber como entrada
# em uma funcao quantos parametros forem necessarios. Eles sao separados por virgula.

# Exemplos


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))


# OBS: Se a gente informar um número errado de parametro ou argumentos, teremos TypeError

#print(soma(2, 3, 4)) # TypeError - Passando argumentos a mais
# print(soma(4))  # TypeError - Passando argumentos a menos

# Nomeando parametros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo eh {nome} {sobrenome}'


print(nome_completo('Angelina', "Jolie"))


# A diferenca entre Parametros e Argumentos

# Parametros sao variaveis declaradas na definicao de uma funcao;
# Argumentos sao dados passados durante a execucao de uma funcao;


# A ordem dos parametros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
"""

# Erro comum na utilizacao do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
