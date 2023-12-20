"""
POO - Classes

Em POO, Classes nada mais sao do que modelos dos objetos do mundo real sendo representados
computacionalmente.

Imagine que voce queira fazer um sistema para automatizar o controle das lampadas da sua casa.


Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lampada, possivelmente
    iriamos querer saber se a lampada eh 110 ou 220 volts, se ela eh branca, amarela, vermelha ou
    outra cor, qual eh a luminosidade dela e etc.

    - Metodos (funcoes) -> Representam os comportamentos do objeto. Ou seja, as acoes que este
    objeto pode realizar no seu sistema. No caso da lampada, por exemplo, um comportamento comum
    que muito provavelmente iriamos querer representar no nosso sistema eh o de ligar e desligar
    a mesma.


Em Python, para definir uma classe utilizamos a palavra reservada class.


OBS: Utiizamos a palavra 'pass' em Python quando temos um bloco de codigo que ainda nao está
implementado.


OBS: Quando nomeamos nossas classes em Python utilizamos por convencao o nome com inicial
em maiusculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em
maiusculo, todas juntas.


Dica Geek: Em computacao nao utilizamos: Acentuacao, caracteres especiais, espacos ou similares
para nomes de classes, atributos, metodos, arquivos, diretorios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos
estes objetos que serao mapeados para classes de entidade.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


class Int:
    pass


valor = int('42')  # cast

print(help(int))

inteiro = Int()
