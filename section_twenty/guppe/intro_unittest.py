"""
Introducao ao modulo Unittest

Unittest -> Testes Unitarios

O que sao testes unitarios?

Testeea forma de se testar unidades individuais de codigo fonte.

Unidades individuais podem ser: funcoes, metodos, classes, modulos etc.

#OBS: Teste unitario naoeespecifico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de entao ganhamos todos os 'assertions' presentes no modulo.

Para rodar os testes, utilizamos unittest.main()


TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Metodo                      Checa que
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               xeverdadeiro
assertFalse(x)              xefalso
assertIs(a, b)              aeb
assertIsNot(a, b)           a naoeb
assertIfNone(x)             xeNone
assertIsNotNone(x)          x naoeNone
assertIn(a, b)              a esta em b
assertNotIn(a, b)           a nao esta em b
assertIsInstance(a, b)      aeinstancia de b
assertNotIsInstance(a, b)   a naoeinstancia de b


Por convencao, todos os testes em um test case, devem ter seu nome
iniciado com test_

# Para executar os testes com unittest

python nome_do_modulo.py


# Para executar os testes com unittest no modo verbose

python nome_do_modulo -v

# Docstrings nos testes

Podemos acrescentar (eerecomendado) docstrings nos nossos testes.
"""

# Pratica - Utilizndo a abordagem TDD
