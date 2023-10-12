"""
Escopo de variaveis

Dois casos de escopo:

1 - Variaveis globais;
    - Variaveis globais sao reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variaveis locais;
    - Variaveis locais sao reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    esta limitado ao bloco onde foi declarada.


Para declarar variaveis em Python fazemos:

nome_da_variavel = valor_da_variavel


Python eh uma linguagem de tipagem dinânima. Isso significa que
ao declararmos uma variavel, nos nao colocamos o tipo de dado dela.
Este tipo eh inferido ao atribuirmos o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42  # Exemplo de variavel global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))


nao_existo = 'Oi'
print(nao_existo)


numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10  # A variavel 'novo' esta declarada localmente dentro do bloco do if. Portanto, eh local
    print(novo)

print(novo)
