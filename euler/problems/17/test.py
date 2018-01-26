import unittest
from solution import number_letter_counts, to_english

class Test(unittest.TestCase):
    def test_to_english(self):
        self.assertEqual(to_english(1), 'one')
        self.assertEqual(to_english(15), 'fifteen')
        self.assertEqual(to_english(20), 'twenty')
        self.assertEqual(to_english(22), 'twenty two')
        self.assertEqual(to_english(60), 'sixty')
        self.assertEqual(to_english(64), 'sixty four')
        self.assertEqual(to_english(100), 'one hundred')
        self.assertEqual(to_english(297), 'two hundred and ninety seven')
        self.assertEqual(to_english(811), 'eight hundred and eleven')
        self.assertEqual(to_english(1000), 'one thousand')

    def test_solution(self):
        self.assertEqual(number_letter_counts(5), 19)
        self.assertEqual(number_letter_counts(1000), 21124)

if __name__ == '__main__':
    unittest.main()
