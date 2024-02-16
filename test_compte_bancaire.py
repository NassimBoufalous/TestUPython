import unittest

class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant

    def obtenir_solde(self):
        return self.solde

class TestCompteBancaire(unittest.TestCase):

    def test_deposer(self):
        compte = CompteBancaire(1000)
        compte.deposer(50)
        self.assertEqual(compte.obtenir_solde(), 1050)

    def test_retirer(self):
        compte = CompteBancaire(80)
        compte.retirer(50)
        self.assertEqual(compte.obtenir_solde(), 30)

    def test_solde_insuffisant(self):
        compte = CompteBancaire(100)
        with self.assertRaises(ValueError):
            compte.retirer(150)

    def test_obtenir_solde(self):
        compte = CompteBancaire(100)
        self.assertEqual(compte.obtenir_solde(), 100)

if __name__ == '__main__':
    unittest.main()
