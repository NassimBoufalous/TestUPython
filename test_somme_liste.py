import unittest

def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

class TestSommeListe(unittest.TestCase):

    def test_liste_vide(self):
        resultat = somme_liste([])
        self.assertEqual(resultat, 0)

    def test_liste_positifs(self):
        resultat = somme_liste([1, 2, 3, 4, 5])
        self.assertEqual(resultat, 15)

    def test_liste_negatifs(self):
        resultat = somme_liste([-1, -2, -3, -4, -5])
        self.assertEqual(resultat, -15)

    def test_liste_melangee(self):
        resultat = somme_liste([-1, 2, -3, 4, -5])
        self.assertEqual(resultat, -3)

if __name__ == '__main__':
    unittest.main()
