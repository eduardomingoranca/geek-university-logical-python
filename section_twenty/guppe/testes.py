import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudavel."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comiga gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente so vive uma vez.'
        )

    def test_domir_pouco(self):
        """Testando o retorno dormingo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado apos dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormingo muito."""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_eh_engracada(self):
        # self.assertEqual( eh _engracada('Sergio Malandro'), False)
        self.assertFalse(eh_engracada('Sergio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engracado')


if __name__ == '__main__':
    unittest.main()
