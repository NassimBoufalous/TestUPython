import unittest
def compter_mots(phrase):
    if not phrase.strip(): 
        return 0
    mots = phrase.split() 
    return len(mots)



class TestCompterMots(unittest.TestCase):

    def test_phrase_non_vide(self):
        self.assertEqual(compter_mots("J'adore le python"), 3)

    def test_phrase_vide(self):
        self.assertEqual(compter_mots(""), 0)

    def test_espaces_supplementaires(self):
        self.assertEqual(compter_mots("Il fait un peu         froid"), 5)

    def test_espaces_seulement(self):
        self.assertEqual(compter_mots("    "), 0)

if __name__ == '__main__':
    unittest.main()
