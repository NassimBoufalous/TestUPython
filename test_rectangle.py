import unittest

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def calculer_surface(self):
        return self.longueur * self.largeur

class TestRectangle(unittest.TestCase):

    def test_calculer_perimetre(self):
        rectangle = Rectangle(4, 3)
        self.assertEqual(rectangle.calculer_perimetre(), 14)

    def test_calculer_surface(self):
        rectangle = Rectangle(4, 3)
        self.assertEqual(rectangle.calculer_surface(), 12)

if __name__ == '__main__':
    unittest.main()
