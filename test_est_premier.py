import unittest

def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

class TestEstPremier(unittest.TestCase):

    def test_nombre_premier(self):
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(3))
        self.assertTrue(est_premier(13))
        self.assertTrue(est_premier(31))

    def test_nombre_non_premier(self):
        self.assertFalse(est_premier(4))
        self.assertFalse(est_premier(10))
        self.assertFalse(est_premier(25))
        self.assertFalse(est_premier(100))

    def test_zero_et_un(self):
        self.assertFalse(est_premier(0))
        self.assertFalse(est_premier(1))

if __name__ == '__main__':
    unittest.main()
