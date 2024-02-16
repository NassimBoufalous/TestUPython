import unittest

def est_palindrome(chaine):
    chaine = chaine.lower().replace(" ", "") 
    chaine_inverse = chaine[::-1]
    return chaine == chaine_inverse

class TestEstPalindrome(unittest.TestCase):

    def test_palindrome_sensible_a_la_case(self):
        self.assertTrue(est_palindrome("Esope reste ici et se repose"))
        self.assertFalse(est_palindrome("Ésope ne reste pas ici et ne se repose pas"))

    def test_palindrome_avec_espaces(self):
        self.assertTrue(est_palindrome("Kayak"))
        self.assertFalse(est_palindrome("Ce n'est pas un palindrome"))

if __name__ == '__main__':
    unittest.main()
