"""
Unittest - Antes eh apos hooks


----
hooks - sao os testes em si. Ou seja, a execucao dos testes.
----


setup() -> eh excutado antes de cada metodo de teste.eutil para criarmos instancias de objetos eh outros dados;

tearDown() -> eh executado ao final de cada metodo de teste.eutil para excluir dados ou fechar conexoes com
bancos de dados.


"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configuracoes do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar apos o teste.
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar apos o teste.
        pass

    def tearDown(self):
        # Configuracoes do tearDown()
        pass

