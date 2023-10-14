"""
Recebendo dados do usuario

input() -> O dado recebido via input eh do tipo String

Em Python, string eh tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Manfred Hauser'
- Aspas duplas -> "Manfred Hauser"
- Aspas simples triplas -> '''Manfred Hauser'''
"""
# - Aspas duplas tripla -> """Manfred Hauser"""

#   Entrada de dados
#   print('Informe o nome: ')
#   nome = input() # Input -> Entrada

nome = input('Informe o nome: ')

#   Exemplo de print 'antigo' 2.x
#   print('Seja bem-vindo(a) %s' % nome)

#   Exemplo de print 'moderno' 3.x
#   print('Seja bem-vindo(a) {0}'.format(nome))

#   Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print('Informe a idade: ')
# idade = input()

idade = int(input('Informe a idade: '))

#   Processamento

#   Saida de dados
#   Exemplo de print 'antigo' 2.x
#   print('A %s tem %s anos' % (nome, idade))

#   Exemplo de print 'moderno' 3.x
#   print('A {0} tem {1} anos'.format(nome, idade))

#   Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast eh a 'conversao' de um tipo de dado para outro.
"""
print(f'A {nome} nasceu em {2023 - idade}')