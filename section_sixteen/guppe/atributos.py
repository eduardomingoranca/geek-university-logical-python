"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos
nos conseguimos representar computacionalmente os estados de um objeto.


Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instancia;
    - Atributos de Classe;
    - Atributos Dinamicos;


# Atributos de instancia: Sao atributos declarados dentro do metodo construtor.

# OBS: Metodo construtor: Eh um metodo especial utilizado para a construcao do objeto.


# Em Java, uma classe Lampada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    public String cor;
    protected Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por convencao, ficou estabelecido que, todo atributo de uma classe eh publico.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da propria classe onde esta declarado,
utiliza-se __ duplo underscore no inicio de seu nome.

Isso eh conhecido tambem como Name Mangling.

# OBS: Lembre-se que isso eh apenas uma convencao, ou seja, a linguagem Python nao
# vai impedrir que facamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.__senha)  # AttributeError


print(user._Acesso__senha)  # Temos acesso. Mas nao deveriamos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()

# O que significa atributos de instancia?

# Significa, que ao criarmos instancias/objetos de uma classe, todas as instancias
# terao estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

# Atributos de classe, sao atributos, claro, que sao declarados diretamente na classe, ou seja,
# fora do contrutor. Geralmente ja inicializamos um valor, e este valor eh compartilhado entre
# todas as instancias da classe. Ou seja, ao inves de cada instancia da classe ter seus proprios
# valores como eh o caso dos atributos de instancia, com os atributos de classe todas as instancias
# terao o mesmo valor para este atributo.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possivel, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possivel, mas incorreto de um atributo de classe

# OBS: Nao precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# sao chamados de atributos estaticos;

"""

# Classes com Atributo de Instancia Publico


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Publicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos Dinamicos -> Um atributos de instancia que pode ser criado em tempo de execucao.

# OBS: O atributo dinamico sera exclusivo da instancia que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinamico em tempo de execucao

p2.peso = '5kg'  # Note que na classe Produto nao existe o atributo peso

print(f'Produto: {p2.nome}, Descricao: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

# print(f'Produto: {p1.nome}, Descricao: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)
