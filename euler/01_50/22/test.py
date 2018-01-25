import unittest
from solution import alphabetic_value, name_score, total_names_score

class Test(unittest.TestCase):
    def test_alphabetic_value(self):
        self.assertEqual(alphabetic_value('a'), 1)
        self.assertEqual(alphabetic_value('A'), 1)
        self.assertEqual(alphabetic_value('b'), 2)
        self.assertEqual(alphabetic_value('B'), 2)

    def test_name_score(self):
        self.assertEqual(name_score('COLIN', 938), 49714)

    def test_total_names_score(self):
        with open('names.txt') as names_file:
            self.assertEqual(total_names_score(names_file.read()), 871198282)

if __name__ == '__main__':
    unittest.main()
